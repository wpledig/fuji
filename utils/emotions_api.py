import urllib
import base64
import json
import pandas as pd
import numpy as np
import requests
import time

def list_aggregate_emotion_per_timestep(rawData, num_frames_per_timestep):

    list_of_emotions = []
    interval_length = 0

    # find interval length between frames
    try:
        for fragment in rawData['fragments']:
            try:
                interval_length = fragment['interval']
                break
            except KeyError:
                continue
    except KeyError:
        pass

    if interval_length == 0:
        # no face events detected
        return [0]
    else:
        continuous_list = []
        for fragment in rawData['fragments']:
            duration = fragment['duration']
            try: 
                events = fragment['events']
                for e in events:

                    if e == []:
                        emotions = {'neutral': 0.0, 'happiness': 0.0, 'surprise': 0.0, 'sadness': 0.0, 'anger': 0.0, 'fear': 0.0}
                        continuous_list.append(emotions)

                    else:
                        interval = e[0]['scores']
                        neutral = float(interval['neutral'])
                        happiness = float(interval['happiness'])
                        surprise = float(interval['surprise'])
                        sadness = float(interval['sadness'])
                        anger = float(interval['anger'])
                        fear = float(interval['fear'])
                        emotions = {'neutral': neutral, 'happiness': happiness, 'surprise': surprise, 'sadness': sadness, 'anger': anger, 'fear': fear}
                        continuous_list.append(emotions)
            except KeyError:
                reps = duration / interval_length       # add this many empty frames (/emotions) to the list
                emotions = {'neutral': 0.0, 'happiness': 0.0, 'surprise': 0.0, 'sadness': 0.0, 'anger': 0.0, 'fear': 0.0}
                for i in range(reps):
                    continuous_list.append(emotions)
        i = 0
        while i < len(continuous_list):

            emotions_list = continuous_list[i:i+num_frames_per_timestep]
            neutral = 0.0
            happiness = 0.0
            surprise = 0.0
            sadness = 0.0
            anger = 0.0
            fear = 0.0
            for e in emotions_list:
                neutral += e['neutral']
                happiness += e['happiness']
                surprise += e['surprise']
                sadness += e['sadness']
                anger += e['anger']
                fear += e['fear']
                step_emotions = {'neutral': neutral, 'happiness': happiness, 'surprise': surprise, 'sadness': sadness, 'anger': anger, 'fear': fear}
            # sum for each value in the emotion dictionary
            sum_emotions = sum(step_emotions.itervalues())
            if sum_emotions == 0.0:
                list_of_emotions.append(('n','n'))
            else:
                # normalized to a sum of 1
                for k,v in step_emotions.iteritems():
                    step_emotions[k] = v/sum_emotions
                list_of_emotions.append(step_emotions)
            i += num_frames_per_timestep
    return list_of_emotions


def travel_to_point(value, center_point, pure_point):

    vector = pure_point - center_point
    final_vector = vector * value
    return final_vector


def emotions_to_arousal_valence(emotions):

    num_emotions = 6
    pure_neutral = np.array([0.5,0.5], dtype=np.float)[np.newaxis].T
    pure_happiness = np.array([1,1], dtype=np.float)[np.newaxis].T
    pure_surprise = np.array([1,0.5], dtype=np.float)[np.newaxis].T
    pure_sadness = np.array([0,0], dtype=np.float)[np.newaxis].T
    pure_anger = np.array([1,0], dtype=np.float)[np.newaxis].T
    pure_fear = np.array([1,0], dtype=np.float)[np.newaxis].T
    point_sum = pure_neutral + pure_happiness + pure_surprise + pure_sadness + pure_anger + pure_fear
    center_point = point_sum/num_emotions

    try:
        neutral_vector = travel_to_point(emotions['neutral'], center_point, pure_neutral)
        happiness_vector = travel_to_point(emotions['happiness'], center_point, pure_happiness)
        surprise_vector = travel_to_point(emotions['surprise'], center_point, pure_surprise)
        sadness_vector = travel_to_point(emotions['sadness'], center_point, pure_sadness)
        anger_vector = travel_to_point(emotions['anger'], center_point, pure_anger)
        fear_vector = travel_to_point(emotions['fear'], center_point, pure_fear)

        final_point = center_point + neutral_vector + happiness_vector + surprise_vector + sadness_vector + anger_vector + fear_vector
        
        arousal = final_point[0][0]
        valence = final_point[1][0]
    except KeyError:
        return ('n', 'n')
    return arousal, valence


def run(rawData, num_frames_per_timestep):

    emotions_list = list_aggregate_emotion_per_timestep(rawData, num_frames_per_timestep)
    arousal_valence_list = []
    for emotions in emotions_list:
        if type(emotions) == type(0) or type(emotions) == type(0.0):
            return []
        elif emotions == ('n', 'n'):
            arousal_valence_list.append(emotions)
        else:
            arousal, valence = emotions_to_arousal_valence(emotions) 
            arousal_valence_list.append((arousal, valence))
    return arousal_valence_list


def run_emotion_api(file_name, _key, music_bpm=120, multiple=16):

    _url = 'https://api.projectoxford.ai/emotion/v1.0/recognizeInVideo'
    _maxNumRetries = 10

    paramsPost = urllib.parse.urlencode({'outputStyle' : 'perFrame', 'file': file_name})
    headersPost = dict()
    headersPost['Ocp-Apim-Subscription-Key'] = _key
    headersPost['content-type'] = 'application/octet-stream'

    try:
        responsePost = requests.request('post', _url + "?" + paramsPost, data = open(file_name,'rb').read(), \
                                        headers = headersPost)
    except IOError:
  
        return

    if responsePost.status_code == 202:
        location = responsePost.headers['Operation-Location']

        ready = False
        while not ready:
            time.sleep(60) # pause program for 60 seconds
            headersGet = dict()
            headersGet['Ocp-Apim-Subscription-Key'] = _key

            jsonGet = {}
            paramsGet = urllib.parse.urlencode({})
            getResponse = requests.request('get', location, json = jsonGet, 
                data = None, headers = headersGet, params = paramsGet)
            try:
                rawData = json.loads(json.loads(getResponse.text)['processingResult'])
                fps = rawData['framerate']
                fps = round(fps)
                num_frames_per_timestep = ((fps*15)/music_bpm)*multiple
                ready = True
            except KeyError:
                continue
        return run(rawData, int(num_frames_per_timestep))
    else:
        #print "unsuccessful"
        return []
