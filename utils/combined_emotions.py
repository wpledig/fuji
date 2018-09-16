from utils.dominant_colors import run_dominant_colors
from utils.emotions_api import run_emotion_api


def video_to_emotion(file_name, music_bpm=120, k=8, multiple=16):
	_key = "49d568ee94764b009dd782ee72ac8b58"

	color_list = run_dominant_colors(file_name, music_bpm, k, multiple)
	emotion_api_list = run_emotion_api(file_name, _key, music_bpm, multiple)

	if emotion_api_list != []:
		while True:
			try:
				i = emotion_api_list.index(('n','n'))
			except ValueError: 
				break
			try:
				emotion_api_list[i] = color_list[i]
			except IndexError:
				break 						

		averaged_emotions_list = [((a_color+a_emotion)/2, (v_color+v_emotion)/2) for (a_color,v_color),(a_emotion, v_emotion) in zip(color_list, emotion_api_list)]
		# add remaining color_list values at the end if color_list is larger than emotion_api_list

		if len(emotion_api_list) < len(color_list):
			emotion_api_list_length = len(emotion_api_list)
			averaged_emotions_list += color_list[emotion_api_list_length:]

	else:
		averaged_emotions_list = color_list
	return averaged_emotions_list


def video_to_emotion_as_file(file_name, music_bpm=120, k=8, multiple=16):

	emotions_list = video_to_emotion(file_name, music_bpm, k, multiple)
	file_name = "sentiment_files/"+file_name.split("/")[-1].split('.')[0]
	f = open('%s.txt' %file_name, 'w+')
	for (a,v) in emotions_list:
		f.write("%f, %f\n" %(a,v))
	f.close()
	return None


if __name__ == "__main__":
	videofile = "/Users/Joel/Desktop/bh_short.mp4"
	video_to_emotion_as_file(videofile, multiple=24)

