from flask import Flask
#from flask import Response, jsonify, request, render_template, send_file
from flask_assistant import Assistant, tell
from flask_cors import CORS
#from pprint import pprint
#import json, jsonify, requests
import GetSnap

app = Flask(__name__)

app.config['ASSIST_ACTIONS_ON_GOOGLE'] = True
app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']

cors = CORS(app)
assist = Assistant(app, route='/google')

@app.route("/", methods=['GET'])
def main():
    return "Eureka"

@assist.action('tv-watch')
def google_tv_watch():
    speech,image,url = GetSnap.return_speech()
    f = open('img.jpg',"wb")
    f.write(image)
    f.close()
    return tell("I see " + speech[:154]).card(
        text="See...",
        title="Image:",
        img_url=url
    )

if __name__ == '__main__':
    app.run(threaded=True, port=5000)