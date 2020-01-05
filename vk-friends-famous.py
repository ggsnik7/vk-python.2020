import requests
import json

f = open('token_gg.txt','r')
token = f.read()
f.close()

params = {'v':'5.52','access_token':token}
r = requests.get('https://api.vk.com/method/friends.get',params=params)
friends = json.loads(r.content)

max_count = 0
max_user_id = 0
for friend in friends['response']['items']:
    params = {'user_id': friend, 'v':'5.52','access_token':token}
    r = requests.get('https://api.vk.com/method/friends.get',params=params)
    friend = json.loads(r.content)
    count = friends['response']['count'] #получить число друзей у друга
    if count > max_count:
        max_count = count
        max_user_id = friend
    else:
        pass
print(max_count,max_user_id)
