import urllib2
import json

def printResponse(response):
    jData = json.loads(response)
    print(jData)

def getData(url):
    return urllib2.urlopen(url).read()

print("Starting...")

# First set up the URL for getting security data from rest-api hosted on Azure
getAllUrl = "http://pythontestweb01-stag.azurewebsites.net/api/security/"
getOneUrl = "http://pythontestweb01-stag.azurewebsites.net/api/security/1"

print("_______________________________________________________")

print("Getting first item for security...")
print("_______________________________________________________")

response = getData(getOneUrl)
printResponse(response)

print("_______________________________________________________")

print("Now getting all available securities ...")
print("_______________________________________________________")

response = getData(getAllUrl)
printResponse(response)


print("Securities downloaded.")
