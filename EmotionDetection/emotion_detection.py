
import requests
import json
'''
emotion detector
'''

URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse):
    Inputjson= { "raw_document": { "text": text_to_analyse } }
    pst = requests.post(URL, headers=HEADERS, json=Inputjson)

    if pst.status_code == 400:
        rsp = {"anger":None, "disgust":None, "fear":None, "joy":None, "sadness":None, 'dominant_emotion':None}

    else:
        rsp = json.loads(pst.text)['emotionPredictions'][0]['emotion']
        em_rating = 0
        top_emotion = 'emotionless'
        
        for emotion in rsp:
            if rsp[emotion] > em_rating:
                em_rating = rsp[emotion]
                top_emotion = emotion

        rsp['dominant_emotion']=top_emotion

    return rsp