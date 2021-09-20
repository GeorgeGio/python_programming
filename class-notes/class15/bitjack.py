import requests
from pprint import pprint


url = 'http://api.giphy.com/v1/gifs/search'
search_term = 'funny avengers'
params = {'q': search_term,
          'api_key': 'dc6zaTOxFJmzC'}
resp = requests.get(url, params=params)
print(resp)
pprint(resp.json())
print(resp.url)
