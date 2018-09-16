import requests
import json


BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com'

CV_URL = BASE_URL + "/vision/v1.0/analyze"
CV_SUBSCRIPTION_KEY1 = "8b631f6e248d4683914ee306d6743165"
CV_SUBSCRIPTION_KEY2 = "6c705160708e4e6e9061f45cabe23519"

FACE_URL = BASE_URL + "/face/v1.0/detect"
FACE_SUBCRIPTION_KEY1 = "49d568ee94764b009dd782ee72ac8b58"
FACE_SUBCRIPTION_KEY2 = "2c38a1a7a32c47138222ccf609ca6314"



def facial_emotions(filename):
    headers = {
         'Content-Type': 'application/octet-stream',
         'Ocp-Apim-Subscription-Key': FACE_SUBCRIPTION_KEY1,
    }

    params = {
        'returnFaceAttributes': 'emotion'
    }

    with open(filename, 'rb') as f:
        img_data = f.read()

    try:
        response = requests.post(FACE_URL,
                                 data=img_data, 
                                 headers=headers,
                                 params=params)
        emotions = {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 0.0, 'neutral': 0.0, 'sadness': 0.0, 'surprise': 0.0}
        faces = response.json()
        for face in faces:
            for emotion in face['faceAttributes']['emotion']:
                emotions[emotion] += face['faceAttributes']['emotion'][emotion]
        for emotion in emotions:
            emotions[emotion]/=max(1, len(faces))

        return emotions

    except Exception as e:
        print('Error:')
        print(e)
        return {}


def image_analysis(filename):
    headers = {
         'Content-Type': 'application/octet-stream',
         'Ocp-Apim-Subscription-Key': CV_SUBSCRIPTION_KEY2,
    }

    params = {
        'visualFeatures': 'Categories,Description,Color'
    }

    with open(filename, 'rb') as f:
        img_data = f.read()

    try:
        response = requests.post(CV_URL,
                                 data=img_data, 
                                 headers=headers,
                                 params=params)
        analysis = response.json()
        return analysis

    except Exception as e:
        print('Error:')
        print(e)
        return {}

    
if __name__ == "__main__":
    filename = 'img/test/brad2.jpg'
    #emotions = facial_emotions(filename)
    #print(emotions)
    analysis = image_analysis(filename)
    for ln in analysis:
        print(ln, analysis[ln])
        print("\n\n")
