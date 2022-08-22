from unittest import result
import requests
import json
link = str('https://americas.api.riotgames.com/lor/ranked/v1/leaderboards?api_key=')
key = str(input(''))
Response_API = requests.get(link + key)
print(Response_API.status_code)

