import urllib.parse
import requests
from pprint import pprint

app_id = 6703233
auth_url = 'https://oauth.vk.com/authorize'
auth_params = {
    'client_id': app_id,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token'
}
print('?'.join((auth_url, urllib.parse.urlencode(auth_params))))
token = 'cfcfed49447ba9173faa7764fe02738d74bb9da002b64a6d2076a0956a4f2c95e54a292f3de989a0cd76c'


par = {
    'access_token': token,
    'user_id': '10951481',
    'v': '5.8'
}
res = requests.get('https://api.vk.com/method/users.get?', par)
pprint(res.json())



# def user_info(self, id):
#     r = 'https://api.vk.com/method/users.get?user_ids={id}&v=5.74'
#     return r

# par = { 
#     'target_uid': '10951481',
#     'v': '5.85'
# }
# response = requests.get('https://api.vk.com/method/friends.getMutual', par)