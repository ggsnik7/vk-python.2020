import requests
import json

f = open('token_gg.txt','r')
token = f.read()
f.close()

r = requests.get('https://api.vk.com/method/friends.getOnline?v=5.52&access_token='+token)
friends = json.loads(r.content)
ch = friends['response']
kol_d = len(ch)


print('Количество друзей:', kol_d)