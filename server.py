import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import moviepy.editor


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "mp4"

def get_file_path(filename):
    return os.path.join(app.config["UPLOAD_FOLDER"], str(filename))

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Johnny Johnny Yes Papa"


@app.route('/upload', methods=['GET', 'POST']) 
def upload():
    print("__UPLOAD__")
    if(request.method == 'POST'):
        file = request.files['file']
        filename = secure_filename(file.filename)
        path = get_file_path(filename)
        file.save(path)
        return redirect(url_for('mp4', filename=filename))
    else:
        assert False


@app.route('/mp4/<filename>')
def mp4(filename):
    path = get_file_path(filename)
    movie = moviepy.editor.VideoFileClip(path)
    print("print -- he movie is {secs} seconds".format(secs = movie.duration))
    return "The movie is {secs} seconds".format(secs = movie.duration)



if __name__ == '__main__':
    app.run(port=5000)
