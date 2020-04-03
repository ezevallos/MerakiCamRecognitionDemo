from flask import Flask, Response, jsonify, request, render_template, send_file
from flask_assistant import Assistant, tell
from flask_cors import CORS
from pprint import pprint
import json, jsonify, requests
import GetSnap
import base64

app = Flask(__name__)

app.config['ASSIST_ACTIONS_ON_GOOGLE'] = True

cors = CORS(app)
assist = Assistant(app, route='/google')

@app.route("/", methods=['GET'])
def main():
    return ""

@app.route("/img", methods=['GET'])
def get_image():
    return send_file('img.jpg', mimetype='image/jpg')

@assist.action('tv-watch')
def google_tv_watch():
    speech,image = GetSnap.return_speech()
    f = open('img.jpg',"wb")
    f.write(image)
    f.close()
    return tell("I see " + speech[:154]).card(
        text="",
        title="See Image:",
        img_url="https://lychee-custard-48379.herokuapp.com/img"
    )

if __name__ == '__main__':
    app.run(threaded=True, port=5000)