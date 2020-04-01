import base64
import requests
import json
import time
from pprint import pprint

def setHeaders_meraki():
    header = {
        "X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
        "Accept":"application/json",
        "Content-Type":"application/json"
    }
    return header

def getSnap(theHeader):
    uri = "https://api.meraki.com/api/v0/networks/L_566327653141856854/cameras/Q2GV-7HEL-HC6C/snapshot?X-Cisco-Meraki-API-Key=6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    resp = requests.post(uri, headers = theHeader,data={})
    return resp.json()

header = setHeaders_meraki()
snapshot = getSnap(header)

pprint(snapshot)

url = snapshot["url"]
print(url)

uri = "https://api.imagga.com/v2/tags"

querystring = {"image_url":url,"version":"2"}

headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjX2RiOWJlYjcwMjhmNjYxNToxYTY3NTQ0YjU5NTBkYTZiYjFmYWY0MjkzNTgzMGZjMg=="
    }

response = requests.request("GET", uri, headers=headers, params=querystring)

print(response.text)

"""
api_key = 'acc_db9beb7028f6615'
api_secret = '1a67544b5950da6bb1faf42935830fc2'
image_url = url

response = requests.get(
    'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
    auth=(api_key, api_secret))

pprint(response.json())
"""
