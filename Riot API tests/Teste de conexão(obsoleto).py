from unittest import result
import requests
import json
Response_API = requests.get('https://americas.api.riotgames.com/lor/ranked/v1/leaderboards?api_key=RGAPI-414e845c-3394-47c2-abcb-4e0f89f81237')
print(Response_API.status_code)
#RGAPI-2f62d7c1-cfa8-4c0f-842a-01ec7f4a1155
