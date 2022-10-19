'''
7. Faça um algoritmo para ler dois vetores V1
   e V2 de 10 números cada. Calcular e escrever
   a quantidade de vezes que V1 e V2 possuem os
   mesmos números e nas mesmas posições.
'''

v1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 10]
v2 = [10, 21, 32, 44, 54, 65, 77, 87, 98, 10]
num_iguais = 0

for i in range(10):
  if v1[i] == v2[i]:
    print(f"{v1[i]} e {v2[i]} são iguais!")
    print(f"Estão os dois na posição {i}")
    num_iguais += 1

print(f"Quantidade de números iguais nas mesmas posições: {num_iguais}")