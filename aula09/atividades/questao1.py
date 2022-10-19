'''
1. Use um dicionário para armazenar informações sobre uma
   pessoa que você conheça. Armazene seu primeiro nome, o
   sobrenome, a idade e a cidade em que ela vive. Você deverá
   ter chaves como primeiro_nome, sobrenome, idade, e cidade.
   Por fim, mostre cada informação armazenada em seu dicionário.
'''

pessoa = {"nome": "Lucas", "sobrenome": "Silva", "idade": 23, "cidade": "João Pessoa"}

for key in pessoa:
  print(pessoa[key])