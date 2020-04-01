import requests
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

def get_image(url):
    code = 404
    while code != 200:
        response = requests.get(url)
        code = response.status_code
    return response.content

def analyze(url, image, key, secret):
    response = requests.post(
        url,
        auth=(key, secret),
        files={'image': image})
    return response

# Vars
imagga_url = 'https://api.imagga.com/v2/tags'
api_key = 'acc_db9beb7028f6615'
api_secret = '1a67544b5950da6bb1faf42935830fc2'

header = setHeaders_meraki()
snapshot = getSnap(header)
image = get_image(snapshot["url"])
response = analyze(imagga_url, image, api_key, api_secret)
pprint(response.json())
