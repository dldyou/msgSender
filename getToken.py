import requests
import json

# get tokens 
url = "https://kauth.kakao.com/oauth/token"
data = {}
with open("./data.json", "r") as f:
    data = json.load(f)

# data looks like -> 
# data = {
#     "grant_type" : "authorization_code",
#     "client_id" : "{REST API}",
#     "redirect_url" : "https://localhost:8000",
#     "code" : "{code}"
# }

res = requests.post(url, data=data)
tokens = res.json()

with open("code.json", "w") as f:
    json.dump(tokens, f)

