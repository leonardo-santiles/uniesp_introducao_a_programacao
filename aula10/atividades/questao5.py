'''
5. Crie um vetor N que seja resultado da soma
   dos itens de outros dois vetores A e B.
   Exemplo: A[0] + B[0] deverá ser salva em N[0].
'''

vetorA = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
vetorB = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vetorN = []

for i in range(10):
  vetorN.append(vetorA[i] + vetorB[i])

print(f"Vetor N: {vetorN}")