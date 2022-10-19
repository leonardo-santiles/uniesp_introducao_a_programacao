'''
8. Faça um algoritmo para ler um vetor de 30 números.
   Após isto, ler mais um número qualquer, calcular e
   escrever quantas vezes esse número aparece no vetor.
'''

vetor = []

while True:
  num = float(input("Digite um número: "))
  vetor.append(num)

  if len(vetor) == 30:
    break

x = float(input("Digite mais um número: "))
ocorrencias = 0

for num in vetor:
  if x == num:
    ocorrencias += 1

print(f"Ocorrências do número {x} no vetor: {ocorrencias}")