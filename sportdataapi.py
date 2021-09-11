import requests
from pprint import pprint
from config import API_KEY_SPORT_DATA

headers = {
  "apikey": API_KEY_SPORT_DATA}

params = (
   ("continent","Asia"),
)

response = requests.get('https://app.sportdataapi.com/api/v1/soccer/countries', headers=headers, params=params);
pprint(response.json())