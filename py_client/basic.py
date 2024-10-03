import requests

endpoint = "http://www.github.com"


response = requests.get(endpoint)

print(response.json())