import requests
import json

def printResponse(response):
    jData = json.loads(response.content)
    print(jData)

print("Starting...")

# First set up the URL for getting security data from rest-api hosted on Azure
getAllUrl = "http://pythontestweb01-stag.azurewebsites.net/api/security/"
getOneUrl = "http://pythontestweb01-stag.azurewebsites.net/api/security/1"

print("Getting first item for security...")

response = requests.get(getOneUrl)
printResponse(response)

print("Now getting all available securities ...")

response = requests.get(getAllUrl)
printResponse(response)

print("Securities downloaded.")
