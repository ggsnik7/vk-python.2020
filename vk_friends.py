import requests
import json

f = open('token_gg.txt','r')
token = f.read()
f.close()

params = {'v':'5.52','access_token':token}
r = requests.get('https://api.vk.com/method/friends.getOnline',params=params)
friends = json.loads(r.content)
ch = friends['response']
kol_d = len(ch)


print('Количество друзей:', kol_d)