from flask import Flask, Response, jsonify, request, render_template
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
    tags = GetSnap.tags
    return str(tags)

@assist.action('tv-watch')
def google_tv_watch():
    data_uri="data:image/jpeg;base64," + str(base64.b64encode(GetSnap.get_image(GetSnap.url)))
    print(data_uri[:70])
    return tell("I see " + GetSnap.speech[:154]).card(
        text=""
        title="See Image:",
        img_url=data_uri
    )

if __name__ == '__main__':
    app.run(threaded=True, port=5000)