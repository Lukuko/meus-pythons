import requests
import json
name = str
rank = int
lp = int
players = [name,'\n', rank,'\n',  lp,'\n',]
link = str('https://americas.api.riotgames.com/lor/ranked/v1/leaderboards?api_key=')
key = str(input(''))
Response_API = requests.get(link + key)
print(Response_API.status_code)
json_data = json.loads(Response_API.text)
print(json_data,players)
