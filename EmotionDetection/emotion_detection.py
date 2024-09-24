"""Module for function emotion detection"""
import json
import requests

def emotion_detector(text_to_analyse):
    """Function for emotion detector"""
    url_domain = "https://sn-watson-emotion.labs.skills.network"
    url = f'{url_domain}/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    formatted_response = json.loads(response.text)
    # check the response status code then get appropriate emotion results
    if response.status_code == 200:
        emotion_results = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_results, key=emotion_results.get)
        emotion_results.update({'dominant_emotion': dominant_emotion})
    elif response.status_code == 400:
        emotion_results = {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }

    return emotion_results
