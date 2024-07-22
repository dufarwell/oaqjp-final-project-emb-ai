
import requests

URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyse):
    Inputjson= { "raw_document": { "text": text_to_analyse } }
    pst = requests.post(URL, headers=HEADERS, json=Inputjson)
    print(pst)
    return pst