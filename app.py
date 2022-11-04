import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def load_form():
	return render_template('upload.html')

@app.route('/gray', methods=['POST'])
def upload_image():
	file = request.files['file']
	filename = secure_filename(file.filename)
	file.save(os.path.join('static/', filename))

	display_message = 'Image successfully uploaded and displayed below.'
	return render_template('upload.html', filename=filename, message=display_message)

@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename=filename))

if __name__ == "__main__":
    app.run()