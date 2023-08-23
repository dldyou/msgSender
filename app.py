import requests
import json

tokens = {}
with open("./code.json", "r") as f:
    tokens = json.load(f)
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + tokens["access_token"]
}
data = {
    "template_object" : json.dumps({ 
        "object_type" : "text",
        "text" : "메시지",
        "link" : {
            "web_url" : "https://www.google.co.kr/",
            "mobile_web_url" : "https://www.google.co.kr/"
        }
    })
}
res = requests.post(url, headers=headers, data=data)
if res.json().get('result_code') == 0:
    print('msg send success.')
else:
    print('msg send error : ' + str(res.json()))