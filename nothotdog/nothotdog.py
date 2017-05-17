import os
import random
from flask import Flask
from flask import jsonify
from flask import request, render_template

tmp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmp_dir)

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
        # Return 400 if no file in request
        if not 'file' in request.files:
            return jsonify({'error': 'no file'}), 400
        # Prepare file
        img_file = request.files['file']
        file_name = img_file.filename
        # Using arbitrary similarity and classification for now
        similarity = round(
            random.uniform(0.0, 1.0), 1
        )
        is_hot_dog = random.randint(0, 1)
        return_packet = {
            'file_name': file_name,
            'similiarty': similarity,
            'is_hot_dog': is_hot_dog
        }
        return jsonify(return_packet)
