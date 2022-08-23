import requests, json

summonerName = str
leagueid = str
summonerid = str
queueType = str
tier = str
rank = str
leaguePoints = int
wins = int
losses = int
hotStreak = bool
veteran = bool
freshBlood = bool
inactive = bool
progress = str
target = int
miniSeries = [losses,progress,target,wins]

Response_API = requests.get('https://americas.api.riotgames.com/lor/ranked/v1/leaderboards?api_key=RGAPI-f094f94f-26f7-46b1-bf92-d7eede598649')
json_data = json.loads(Response_API.text)
print(json_data,summonerName)






#players = [name,'\n', rank,'\n',  lp,'\n',]
#Response_API = requests.get('https://americas.api.riotgames.com/lor/ranked/v1/leaderboards?api_key=RGAPI-2f62d7c1-cfa8-4c0f-842a-01ec7f4a1155')
#print(Response_API.status_code)
#json_data = json.loads(Response_API.text)
#print(json_data,players)

