from utils import cv
from utils import combined_emotions as emotions
from utils import generate_midi as generate
import moviepy.editor


def mp4parse(file_path, new_file_path):
    file = moviepy.editor.VideoFileClip(file_path)
    file = file.subclip(0, 60)
    audio = file.audio
    new_audio = fetch_audio(file, file_path).subclip(0, file.duration)
    print(new_audio.duration, file.duration)
    file_edited = file.set_audio(new_audio)
    file_edited.write_videofile(new_file_path)


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


def generate_audio(file, sentiment_file_path):
    midi_file_path = "/Users/Joel/Desktop/hr8/midi/"+sentiment_file_path.split("/")[-1].split(".")[0]+".mid"
    print(midi_file_path)
    #generate.generate_music(sentiment_file_path, midi_file_path)

    ###############################################################

    ##         TODO: GENERATE AUDIO + CONVERT TO MP3

    ###############################################################
    
    audio = moviepy.editor.AudioFileClip("mp4/sweet.mp3")
    return audio


def fetch_audio(file, file_path):
    #video_sum = 0
    #print("fetching audio")
    #num_steps = 10
    #step = file.duration/num_steps
    #print(step)
    #for t in range(0, int(file.duration), int(step)):
        #frame = file.get_frame(t)
        #video_sum+=frame_anal(frame)
    #print("Composite video score: "+str(video_sum))
    emotions.video_to_emotion_as_file(file_path, multiple=24) # generates sentiment_files/<filename>.
    sentiment_file_path = "/Users/Joel/Desktop/hr8/sentiment_files/"+file_path.split("/")[-1].split(".")[0]+".txt"
    print(sentiment_file_path)
    return generate_audio(file, sentiment_file_path)


if __name__ == "__main__":
    generate.generate_music("/Users/Joel/Desktop/hr8/sentiment_files/bh.txt", "/Users/Joel/Desktop/hr8/midi/bh.midi")
