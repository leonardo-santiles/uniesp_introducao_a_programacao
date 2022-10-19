'''
1. Escreva um algoritmo que permita a leitura dos nomes
   de 10 clubes de futebol e armazene os nomes lidos em
   um vetor (lista). Após isto, o algoritmo deve permitir
   a leitura de mais 1 nome qualquer de clube e depois
   escrever a mensagem ACHEI, se o nome estiver entre os
   10 nomes lidos anteriormente (guardados no vetor), ou
   NÃO ACHEI caso contrário.
'''

clubes = []

while True:
  clube = input("Clube que deseja armazenar: ")
  clubes.append(clube)

  if len(clubes) == 10:
    break

clube = input("Clube que deseja buscar: ")

if clube in clubes:
  print("ACHEI")
else:
  print("NÃO ACHEI")