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
        return redirect(url_for('testmp4', filename=filename))
    else:
        assert False


@app.route('/parsemp4/<filename>')
def parsemp4(filename):
    movie_path = get_file_path(filename)
    movie = moviepy.editor.VideoFileClip(movie_path)
    audio = movie.audio # 
    movie_edited = videoclip.set_audio(my_audioclip)
    movie_edited_path = get_file_path()
    return send_file(path)

@app.route('/testmp4/<filename>')
def testmp4(filename):
    file_path = get_file_path(filename)
    file = moviepy.editor.VideoFileClip(file_path)
    file_edited = file.subclip(0, 60).volumex(5.5)
    name, xtn = filename.split(".")
    write_path = get_file_path(name+"_edited."+ xtn)
    file_edited.write_videofile(write_path)
    return send_file(write_path)
    #file_audio = bh.audio

    #movie_path = get_file_path("test.mp4")
    #movie = moviepy.editor.VideoFileClip(movie_path)

    #movie_edited = movie.set_audio(bh_audio)


    #movie_edited_filename = "movie-edited.mp4"
    #movie_edited_path = get_file_path(movie_edited_filename)
    #movie_edited.write_videofile(movie_edited_path)
    #return send_file(movie_edited_path)




if __name__ == '__main__':
    app.run(host = '127.0.0.1', port=5000)
