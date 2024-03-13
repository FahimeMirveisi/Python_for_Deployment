import requests


response = requests.get("https://the-one-api.dev/v2/book")
print(response.status_code)
response.json()


response = requests.get("https://the-one-api.dev/v2/movie")
print(response.status_code)
response.json()