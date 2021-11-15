from pprint import pprint
import requests
import json

# Vars
imagga_url = 'https://api.imagga.com/v2/tags'
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Helper functions
def setHeaders_meraki():
    header = {
        "X-Cisco-Meraki-API-Key":"6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
        "Accept":"application/json",
        "Content-Type":"application/json"
    }
    return header

def getSnap(theHeader):
    uri = "https://api.meraki.com/api/v1/devices/Q2GV-7HEL-HC6C/camera/generateSnapshot?X-Cisco-Meraki-API-Key=6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
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

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 = str1 + ele + ","
    
    str1 = str1[:415]
    while(str1[-1]!=','):
        str1 = str1[:-1]
    str1 = str1[:-1]
    # return string   
    return str1


# return speech function
def return_speech():
    header = setHeaders_meraki()
    snapshot = getSnap(header)
    url = snapshot["url"]
    print(40*"-")
    print(url)
    print(40*"-")
    image = get_image(url)
    response = analyze(imagga_url, image, api_key, api_secret)
    pprint(response.json(), indent=2, width=200)
    print(40*"-")
    tags = [item['tag']['en'] for item in response.json()['result']['tags']]
    speech = listToString(tags)
    return (speech, url)
