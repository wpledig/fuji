import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Johnny Johnny Yes Papa"


@app.route('/upload', methods=['GET', 'POST'])
def upload():
<<<<<<< HEAD
    if(request.method == 'GET'):
        print("----------")
        return "-------"
    else:
        print("___UPLOAD___")
        print(request)
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))
=======
    print("___UPLOAD___")
    print(request)
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('uploaded_file', filename=filename))
>>>>>>> da48a8dcb52994493d9e2564549df8cf109bd795



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return "Hello World"



if __name__ == '__main__':
    app.run(port=5000)
