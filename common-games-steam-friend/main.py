import json
import requests
from requests_html import HTMLSession
import os
from dotenv import load_dotenv
load_dotenv()

print('Accounts must be "public".')

firstPlayer = input("SteamID of the first Steam account : \n")
secondPlayer = input("SteamID of the second Steam account : \n")

steam_api_key = os.getenv('key')

response = requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steam_api_key}&steamid={firstPlayer}&format=json')
jsonReturns = json.loads(response.text)
liststeam = jsonReturns["response"]
listgames = liststeam["games"]
firstappidlist = []
for appid in listgames:
    firstappidlist.append(appid.get('appid'))

response = requests.get(f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={steam_api_key}&steamid={secondPlayer}&format=json')
jsonReturns = json.loads(response.text)
liststeam = jsonReturns["response"]
listgames = liststeam["games"]
secondappidlist = []
for appid in listgames:
    secondappidlist.append(appid.get('appid'))

l1 = set(firstappidlist)
l2 = set(secondappidlist)
matchappid = l1 & l2

session = HTMLSession()
matchesGames = []
for appid in matchappid:
    url = f'https://steamdb.info/app/{appid}/'
    API = session.get(url)
    title = API.html.find("div.pagehead > h1", first=True)
    matchesGames.append(title.text)

matchesGames.sort()
print("List of common games :")
for games in matchesGames:
    print(games)