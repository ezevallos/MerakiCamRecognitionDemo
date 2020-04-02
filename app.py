from flask import Flask, request, render_template
from pprint import pprint
import json, jsonify, requests
import GetSnap

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    tags = GetSnap.tags
    return str(tags)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)