import os
from flask import *
from werkzeug.utils import secure_filename
import moviepy.editor


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "mp4"

def get_file_path(filename):
    return os.path.join(app.config["UPLOAD_FOLDER"], str(filename))


@app.route('/', methods=['GET', 'POST'])
def index():
    return "'Johnny Johnny Yes Papa' -- Will Ledig (2018)"


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

    #print("mp4 parsing")
    file_path = get_file_path(filename)
    file = moviepy.editor.VideoFileClip(file_path)
    audio = file.audio

    new_audio = fetch_audio(file)
    file_edited = file.set_audio(new_audio)
    file_edited.write_videofile(new_file_path)
    #print("sending")
    return send_file(new_file_path)

def frame_anal(frame):
    #print("frame-anal")
    frame_sum = 0
    pixel_count = 0.0
    for row in frame:
        for pixel in row:
            frame_sum+=sum(pixel)/len(pixel)
            pixel_count+=1.0
    print(frame_sum, pixel_count)
    return frame_sum/pixel_count


def fetch_audio(file):
    video_sum = 0
    #print("fetching audio")
    num_steps = 10
    step = file.duration/num_steps
    #print(step)
    for t in range(0, int(file.duration), int(step)):
        frame = file.get_frame(t)
        video_sum+=frame_anal(frame)
    #print("Composite video score: "+str(video_sum))
    return generate_audio(file, video_sum)


def generate_audio(file, video_sum):
    #print("generating audio")
    return file.audio


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port=5000)
