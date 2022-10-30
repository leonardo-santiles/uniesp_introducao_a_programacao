'''
1. Construa uma matriz A de tamanho 10 x 10 com valores
   inteiros e randômicos:
   a. Imprima o resultado da soma de todos os valores da
      matriz no terminal;
   b. Criei uma nova matriz B, no qual cada item seja o
      valor da matriz A * 3
'''

from random import randint

matrizA = []

for i in range(10):
  aux = []
  
  for j in range(10):
    aux.append(randint(0, 100))
  
  matrizA.append(aux)

soma = 0

for linha in matrizA:
  for num in linha:
    soma += num

matrizB = []

for linha in matrizA:
  aux = []

  for num in linha:
    aux.append(num * 3)

  matrizB.append(aux)

print(f"Matriz A: {matrizA}")
print(f"Soma dos números da matriz A: {soma}")
print(f"Matriz B: {matrizB}")