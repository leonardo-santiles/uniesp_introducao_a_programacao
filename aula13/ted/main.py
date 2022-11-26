import requests
import json

API_KEY = ''

with open('data.txt', 'r') as data:
  for linha in data:
    nome, cap, lon, lat = linha.split(', ')

    nome = nome.strip()
    cap = cap.strip()
    lon = lon.strip()
    lat = lat.strip()

    url = (f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}')

    resp = requests.request("GET", url)
    obj = json.loads(resp.text)

    with open(f'./out/{nome}.json', 'w') as file:
      json.dump(obj, file);

print('Fim')
