import requests


from pprint import pprint


url = 'http://api.openweathermap.org/data/2.5/weather'

params = {'q' : 'London',
          'appid' : 'fca2c0c3ea8b930b0d0d9800497f7c88' }

resp = requests.get(url , params=params)

resp.raise_for_status()

data = resp.json()
pprint(data)

current, max_temp, min_temp = data['main']['temp'],data['main']['temp_max'],data['main']['temp_min']

description, city = data['weather'][0]['description'], data['name']


my_string = f"City: {city}\nCurrent: {current}\nMax: {max_temp}\nMin: {min_temp}\nDescription: {description}\n"
print(my_string)
