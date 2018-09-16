import os
import video
from flask import *
import generate_midi as generate
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "mp4"

def get_file_path(filename):
    return os.path.join(app.config["UPLOAD_FOLDER"], str(filename))


@app.route('/', methods=['GET', 'POST'])
def index():
    #generate.generate_music("/Users/Joel/Desktop/hr8/sentiment_files/bh.txt", "/Users/Joel/Desktop/hr8/midi/bh.midi")
    return "'Johnny Johnny Yes Papa!' -- Will Ledig (2018)"


@app.route('/upload', methods=['GET', 'POST']) 
def upload():
    if(request.method == 'POST'):
        file = request.files['file']
        filename = secure_filename(file.filename)
        path = get_file_path(filename)
        file.save(path)
        return redirect(url_for('parsemp4', filename=filename))
    else:
        assert False


@app.route('/parsemp4/<filename>')
def parsemp4(filename):
    name, xtn = filename.split(".")
    new_filename = name+"_edited."+ xtn
    new_file_path = get_file_path(new_filename)
    if(os.path.isfile(new_file_path)):
        return send_file(new_file_path)

    video.mp4parse(get_file_path(filename), new_file_path)
    return send_file(new_file_path)


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port=5000)
