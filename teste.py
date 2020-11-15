import requests

data = {}
data['loginname'] = "rafael"
data['password'] = "tctetscfe"
print(data)


headers = {}
headers['content-type'] = "application/json"

txt = requests.post("https://calm-hamlet-60163.herokuapp.com/auth",headers=headers,data=str(data).replace("'",'"')).json()
print(txt['data']['token'])

token = txt['data']['token']

data = {}
data['token'] = token

txt = requests.post("https://calm-hamlet-60163.herokuapp.com/customers/get",headers=headers,data=str(data).replace("'",'"')).json()
print(txt)
