import os
from flask import Flask
from flask import jsonify
from flask import render_template

tmp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmp_dir)

"""
Index view
"""
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/is-hot-dog', methods=['POST'])
def is_hot_dog():
    return_packet = {
        'similiarty': 0.5,
        'is_hot_dog': False
    }
    return jsonify(return_packet)