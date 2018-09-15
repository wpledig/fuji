import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import moviepy.editor


UPLOAD_FOLDER = '/mp4'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Johnny Johnny Yes Papa"


@app.route('/upload', methods=['GET', 'POST']) 
def upload():
    if(request.method == 'POST'):
        file = request.files['mp4-attachment']
        filename = secure_filename(file.filename)
        file.save(str(filename))
        return redirect(url_for('mp4', filename=filename))
    else:
        assert False


@app.route('/mp4/<filename>')
def mp4(filename):
    movie = moviepy.editor.VideoFileClip(filename)
    print("print -- he movie is {secs} seconds".format(secs = movie.duration))
    return "The movie is {secs} seconds".format(secs = movie.duration)



if __name__ == '__main__':
    app.run(port=5000)
