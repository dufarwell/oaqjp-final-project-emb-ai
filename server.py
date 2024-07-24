from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route('/')
def test():
    print('test')
    return {'message':'test worked'}

@app.route('/emotionDetector')
def emotion_test():
    text_to_test = request.args.get("text_to_test").replace("%20"," ")
    res = emotion_detector(text_to_test)
    rtrn = "For the given statement, the system response is "
    for emotion in [r for r in res if not r == 'dominant_emotion']:
        rtrn += f"'{emotion}': {res[emotion]}, "
    rtrn = rtrn[:-2] + f". The dominant emotion is {res['dominant_emotion']}."
    print(rtrn)
    return rtrn