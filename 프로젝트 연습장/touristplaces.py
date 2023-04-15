import requests
import pprint
import urllib.parse
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db= client.google_map

city = ["Berkeley", "Sanfrancisco", "OaklandCA", "LosAngeles", "Sanjose"]

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=tourist%20in%20Sanfrancisco&key=AIzaSyCcvW8a-l-tXtMKVwuu_5syXQdDRAvb3L0"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print (response.text)