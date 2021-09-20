import requests


from pprint import pprint


url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)


print(response)
data = response.json()
people = data['people']
for person in people:

    print(f'{person["name"]} in onboard the {person["craft"]} space station.')
