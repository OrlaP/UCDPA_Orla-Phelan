import requests

url = "https://wine-recognition2.p.rapidapi.com/v1/version"

headers = {
    'x-rapidapi-key': "47b4b95695mshddb0626cdd6e928p161db1jsn704979346acd",
    'x-rapidapi-host': "wine-recognition2.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

url = "https://wine-recognition2.p.rapidapi.com/v1/results"

querystring = {"n": "10"}

payload = "url=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fa%2Fad%2FFumin_varietal_wine_1.jpg"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "47b4b95695mshddb0626cdd6e928p161db1jsn704979346acd",
    'x-rapidapi-host': "wine-recognition2.p.rapidapi.com"
    }
response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
