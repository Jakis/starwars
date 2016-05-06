#!/usr/bin/python

import requests
import json

# Pull json data for a given swapi url
def getData (url):
    headers = {'User-Agent': 'starwarspy'}
    response = requests.get(url, headers=headers)
    jsonData = response.json()
    return jsonData

def printShips(jsonResponse):
    for item in jsonResponse['results']:
        print "SHIP : %s" % item['name']
        if len(item['pilots']) > 0:
            print "PILOTS: " 
            for i in item['pilots']:
                print " - %s" % getData(i)['name']
        else:
            print "no pilots on record"
        print ""

url = 'http://swapi.co/api/starships/'
jsonResponse = getData(url)
printShips(jsonResponse)

while (jsonResponse['next'] != None):
    url = jsonResponse['next']
    jsonResponse = getData(url)
    printShips(jsonResponse)
