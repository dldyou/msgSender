import time
import threading
import requests
import json
import sys

tokens = {}
users = {}
with open("./code.json", "r") as f:
    tokens = json.load(f)
with open("./user.json", "r") as f:
    users = json.load(f)
    
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + tokens["access_token"]
}
data = {}

def setData(text, url):
    global data
    data = {
        "template_object" : json.dumps({ 
            "object_type" : "text",
            "text" : text + f'\n{url}',
            "link" : {
                "web_url" : url,
                "mobile_web_url" : url
            }
        })
    }
    
def sendMsg():
    res = requests.post(url, headers=headers, data=data)
    if res.json().get('result_code') != 0:
        print('msg send error : ' + str(res.json()))
        
def findUser(handle):
    url = "https://solved.ac/api/v3/search/user"
    querystring = {"query": handle,"page": "1"}
    headers = {"Accept": "application/json"}
    res = requests.get(url, headers=headers, params=querystring).json()
    return res

def addUser(handle):
    global users
    print(f'add user: {handle}')
    if(handle in users):
        print("해당 유저가 이미 추가된 상태입니다.")
        return
    res = findUser(handle)
    if (res["count"] == 0):
        print("해당 유저가 존재하지 않습니다.")
        return
    user = res["items"][0]
    if (user["handle"] != handle):
        print("해당 유저가 존재하지 않습니다.")
        return
    
    print(f'solved: {user["solvedCount"]}')
    users[handle] = {"solved": user["solvedCount"]}
    with open("./user.json", "w") as f:
        json.dump(users, f)

def check():
    global users
    for handle in users.keys():
        solved = findUser(handle)["items"][0]["solvedCount"]
        if (solved != users[handle]["solved"]):
            print(f'{handle}님이 새로운 문제를 풀었습니다!')
            setData(f'{handle}님이 새로운 문제를 풀었습니다!', f'https://www.acmicpc.net/status?problem_id=&user_id={handle}&language_id=-1&result_id=-1')
            sendMsg()
            
            users[handle]["solved"] = solved
            with open("./user.json", "w") as f:
                json.dump(users, f)
        else:
            print(f'{handle}님이 아직 문제를 안 풀었습니다')
    threading.Timer(60, check).start()

def main():
    argv = sys.argv
    if (len(argv) == 1): # standard mode
        check()
    elif (len(argv) == 3): # add user
        if (argv[1] == "-add"): # add user
            addUser(argv[2])
    
if __name__ == "__main__":
    main()