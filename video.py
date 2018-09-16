import cv
import moviepy.editor


def mp4parse(file_path, new_file_path):
    file = moviepy.editor.VideoFileClip(file_path)
    file = file.subclip(0, file.duration - 60)
    audio = file.audio
    new_audio = fetch_audio(file).subclip(0, file.duration)
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


def generate_audio(file, video_sum):
    #print("generating audio")
    audio = moviepy.editor.AudioFileClip("mp4/sweet.mp3")
    return audio


def fetch_audio(file):
    video_sum = 0
    #print("fetching audio")
    num_steps = 10
    step = file.duration/num_steps
    #print(step)
    for t in range(0, int(file.duration), int(step)):
        frame = file.get_frame(t)
        #video_sum+=frame_anal(frame)
    #print("Composite video score: "+str(video_sum))
    return generate_audio(file, video_sum)

