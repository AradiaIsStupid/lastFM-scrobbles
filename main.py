import requests
from datetime import datetime 
import asciilist
import random
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY= os.getenv("API_KEY")
USERNAME = os.getenv("USERNAME")
API_URL= 'https://ws.audioscrobbler.com/2.0/'

timern = datetime.now()
timern_inseconds = timern.strftime('%s')
timeyd_inseconds = int(timern_inseconds) - 86400
params = {
    'method': 'user.getRecentTracks',
    'user': USERNAME,
    'api_key': API_KEY,
    "format": 'json',
    'limit': 1000,
    'from': timeyd_inseconds,
    'to':timern_inseconds,
}

asciilist=[asciilist.ascii1, asciilist.ascii2]

response = requests.get(API_URL, params=params)
if response.status_code == 200: 
    data = response.json()
    if 'recenttracks' in data and 'track' in data['recenttracks']:
        scrobble_count = len(data['recenttracks']['track'])
        asciiart = random.choice(asciilist)
        print(asciiart)
        print(f'You have scrobbled {scrobble_count} tracks from yesterday to today on Last.fm.')
    else:
        print('No scrobbles found for the specified date range.')
else:
    print('Failed to retrieve data from Last.fm API.') 
