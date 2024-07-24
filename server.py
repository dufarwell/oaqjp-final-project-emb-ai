from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)

@app.route('/')
def test():
    print('test')
    return {'message':'test worked'}

@app.route('/text/<text_to_test>')
def emotion_test(text_to_test):
    print(text_to_test)
    res = emotion_detector(text_to_test)
    print(res)