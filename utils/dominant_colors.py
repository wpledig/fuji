from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
import numpy as np
import itertools
from math import factorial
from tqdm import tqdm
import moviepy.editor as mp


def centroid_histogram(clt):

	numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins=numLabels)

	hist = hist.astype("float")
	hist /= hist.sum()

	return hist


def color_to_valence(color):

	# values are between 0-255
	s = float(color[1])			
	v = float(color[2])			

	average_valence = (s+v)/2
	normalised_valence = average_valence/255
	return normalised_valence


def travel_to_point(value, center_point, pure_point):

	vector = pure_point - center_point
	final_vector = vector * value
	return final_vector


def shortest_distance(v):

	x,y = v
	x = int(x)
	y = int(y)
	return min(abs(x-y), 180-abs(x-y))


def calculate_arousal_from_color_diversity(color_list, max_distance):

	total_distance = 0
	hue_list = []
	for color, _ in color_list:
		hue_list.append(color[0])
	# sums the shortest distances for all unique combinations of hue pairs  
	for pair in itertools.combinations(hue_list, 2):
		total_distance += shortest_distance(pair)

	# TODO: exception handling if return is larger than 1
	normalised_arousal = float(total_distance)/max_distance	# normalize so value is between 0 and 1
	return normalised_arousal


def averaged_emotion(color_list, k):

	center_point = np.array([0.5,0.5], dtype=np.float)[np.newaxis].T
	final_point = center_point

	# find maximum distance given all points are equidistant from one another
	equidistance = float(180)/k
	equidistant_list = []
	for x in range(k):
		equidistant_list.append(x*equidistance)

	max_distance = 0
	for max_pair in itertools.combinations(equidistant_list, 2):
		max_distance += shortest_distance(max_pair)

	# calculate arousal and valence values
	arousal = calculate_arousal_from_color_diversity(color_list, max_distance)
	for color,percent in color_list:
		valence = color_to_valence(color)
		point = np.array([arousal,valence], dtype=np.float)[np.newaxis].T
		color_point_vector = travel_to_point(percent, center_point, point)
		final_point += color_point_vector

	arousal = final_point[0][0]
	valence = final_point[1][0]
	return arousal, valence


def run_dominant_colors(file_name, music_bpm=120, k=8, multiple=16):

	
	cap = cv2.VideoCapture(file_name)
	ret = True
	fps = cap.get(cv2.CAP_PROP_FPS) 
	fps = round(fps)
	num_frames_per_timestep = ((fps*15)/music_bpm)*multiple
	length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 	
	emotions_list_per_timestep = []
	with tqdm(total=length) as pbar:
		while ret:
			pbar.update(1)
			frame_num = int(round(cap.get(1))) 
			ret, frame = cap.read()
			if frame is None:
				break

			if frame_num % num_frames_per_timestep == 0.0:
				frame = cv2.resize(frame, (480,360))
				color_list = []
				image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)					# convert to HSV color space
				image = image.reshape((image.shape[0] * image.shape[1], 3))

				clt = KMeans(n_clusters=k)
				clt.fit(image)
				hist = centroid_histogram(clt)
				centroids = clt.cluster_centers_

				for color_pair in zip(centroids, hist):	
					color_list.append(color_pair)

				emotions_list_per_timestep.append(averaged_emotion(color_list, k))
	pbar.close()
	cap.release()
	cv2.destroyAllWindows()
	return emotions_list_per_timestep

