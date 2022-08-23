import requests
import json

name = str
rank = int
lp = int
players = [name,'\n', rank,'\n',  lp,'\n',]
Response_API = requests.get('https://americas.api.riotgames.com/lor/ranked/v1/leaderboards?api_key=RGAPI-f094f94f-26f7-46b1-bf92-d7eede598649')
print(Response_API.status_code)
json_data = json.loads(Response_API.text)
print(json_data,players)
#RGAPI-2f62d7c1-cfa8-4c0f-842a-01ec7f4a1155
