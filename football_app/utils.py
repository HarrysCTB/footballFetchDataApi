import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_data_from_api():
    url = 'https://api.football-data.org/v4/matches'
    headers = { 'X-Auth-Token': os.getenv('X_AUTH_TOKEN') }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None