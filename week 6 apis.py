import requests

request = requests.get('http://api.open-notify.org/')

print(request.status_code)

print(request.text)

request = requests.get('http://api.open-notify.org/iss-now.json')

print(request.json())

request = requests.get('http://api.open-notify.org/astros.json')

print(request.json())
data=request.json()
print(data['number'])
