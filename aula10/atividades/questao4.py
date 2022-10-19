'''
4. Ler um vetor A de 10 números. Após, ler mais um
   número e guardar em uma variável X. Armazenar em
   um vetor M o resultado de cada elemento de A
   multiplicado pelo valor X. Logo após, imprimir o
   vetor M.
'''

vetorA = []

while True:
  num = int(input("Digite um número inteiro: "))
  vetorA.append(num)

  if len(vetorA) == 10:
    break

x = int(input("Digite mais um número inteiro: "))

vetorM = []
for num in vetorA:
  vetorM.append(num * x)

print(f"Vator M: {vetorM}")