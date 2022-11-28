import requests
import json

API_KEY = '';
cidades = [];

def obter_dados():
  nome = input("Digite o nome da cidade: ").strip();
  lat = input("Digite a latitude: ").strip();
  lon = input("Digite a longitude: ").strip();
  return nome, lat, lon

def cadastrar_cidade():
  nome, lat, lon = obter_dados();
  
  cidade = [nome, lat, lon];
  cidades.append(cidade);
  
def verificar_cidades():
  for cidade in cidades:
    print(f'Cidade: {cidade[0]}, Lat: {cidade[1]}, Lon: {cidade[2]}');

def open_weather(nome, lat, lon):
  url = (f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}');
  resp = requests.request("GET", url);
  obj = json.loads(resp.text);

  with open(f'{nome}.json', 'w') as file:
      json.dump(obj, file);

def open_weather_cidades():
  for cidade in cidades:
    open_weather(cidade[0], cidade[1], cidade[2]);

while True:
  print("Opção   | Descrição")
  print("  1     | Cadastrar uma cidade")
  print("  2     | Verificar cidades cadastradas")
  print("  3     | Chamar a API Open Weather para uma cidade")
  print("  4     | Chamar a API Open Weather para as cidades cadastradas")
  print("  5     | Sair do programa")

  try:
    opcao = int(input("Digite a opção desejada: "))
  except ValueError as error:
    print(f"{error}");
    print("Por favor, digite uma opção válida!")
    continue;

  if opcao == 1:
    cadastrar_cidade();
  elif opcao == 2:
    verificar_cidades();
  elif opcao == 3:
    nome, lat, lon = obter_dados();
    open_weather(nome, lat, lon);
  elif opcao == 4:
    open_weather_cidades();
  elif opcao == 5:
    print('Fim')
    break;
