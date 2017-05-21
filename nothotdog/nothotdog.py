import os
import random
from flask import Flask
from flask import jsonify
from flask import request, url_for, render_template
from rekognition import Rekognition 

rekognizer = Rekognition()

tmp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask(__name__, template_folder=tmp_dir)
app.config['UPLOAD_FOLDER'] = 'static/img'

valid_extensions = ['jpeg', 'jpg', 'png']

"""
Index view
"""
@app.route('/')
def index():
    return render_template('index.html')

"""
Endpoint for hot dog checking
"""
@app.route('/is-hot-dog', methods=['POST'])
def is_hot_dog():
    if request.method == 'POST':
        if not 'file' in request.files:
            return jsonify({'error': 'no file'}), 400

        img_file = request.files.get('file')
        img_name = img_file.filename
        img_split = img_name.split('.')
        img_extension = img_split[len(img_split) - 1]
        if not img_extension in valid_extensions:
            return jsonify({'error': 'bad-type'})

        img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], img_name))
        hot_dog_conf = rekognizer.get_confidence(img_name)
        is_hot_dog = 'false' if hot_dog_conf == 0 else 'true'
        return_packet = {
            'is_hot_dog': is_hot_dog,
            'confidence': hot_dog_conf
        }
        return jsonify(return_packet)
