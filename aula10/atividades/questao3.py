'''
3. Ler um vetor Q de 20 posições (aceitar somente números positivos).
   Escrever a seguir:
   a. o valor do maior elemento de Q e a respectiva posição que ele
      ocupa no vetor;
   b. o valor do menor elemento de Q e a respectiva posição que ele
      ocupa no vetor.
'''

vetorQ = []

while True:
  num = float(input("Digite um número: "))

  if num < 0:
    print("Digite apenas números positivos!")
    continue
  
  vetorQ.append(num)
  
  if len(vetorQ) == 20:
    break

maior = vetorQ[0]
menor = vetorQ[0]

for num in vetorQ:
  if num > maior:
    maior = num

  if num < menor:
    menor = num

print(f"Maior valor {maior} e seu índice {vetorQ.index(maior)}")
print(f"Menor valor {menor} e seu índice {vetorQ.index(menor)}")