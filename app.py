from flask import Flask, request, render_template
from flask_assistant import Assistant, tell
from pprint import pprint
import json, jsonify, requests
import GetSnap

app = Flask(__name__)
assist = Assistant(app, route='/google')

@app.route("/", methods=['GET'])
def main():
    tags = GetSnap.tags
    return str(tags)

@assist.action('tv-watch')
def google_tv_watch():
    print(GetSnap.tags)
    return tell(GetSnap.tags)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)