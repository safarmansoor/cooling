from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    uploaded_file.save(secure_filename(uploaded_file.filename))
    return 'File uploaded successfully'

@app.route('/search', methods=['POST'])
def search():
    search_input = request.form['search_input']
    input_file = request.form['input_file']
    output_file = request.form['output_file']
    
    # code for file search here
    
    return 'File search complete'
