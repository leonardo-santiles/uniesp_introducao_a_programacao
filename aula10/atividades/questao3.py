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
  
  if len(vetorQ) == 3:
    break

maior = max(vetorQ)
posicao_maior = vetorQ.index(maior)
print(f"Valor do maior elemento: {maior}")
print(f"Posição do maior elemento no vetor: {posicao_maior}")


menor = min(vetorQ)
posicao_menor = vetorQ.index(menor)
print(f"Valor do menor elemento: {menor}")
print(f"Posição do menor elemento no vetor: {posicao_menor}")