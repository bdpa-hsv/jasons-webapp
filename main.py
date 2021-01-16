from flask import Flask, render_template  # Import Flask Class
app = Flask(__name__) # Create an Instance

@app.route('/') # Route the Function
def main(): # Run the function
	return render_template('index.html') # Render the template

@app.route('/Search')
def search():
  return render_template('search.html')

@app.route('/Register')
def register():
  return render_template('registration.html') 

@app.route('/Uploads')
def uploads():
  return render_template('uploads.html')
 

app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


