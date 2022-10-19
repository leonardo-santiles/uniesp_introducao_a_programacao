'''
6. Faça um algoritmo para ler um vetor de 20 números.
   Após isto, deverá ser lido mais um número qualquer
   e verificar se esse número existe no vetor ou não.
   Se existir, o algoritmo deve gerar um novo vetor
   sem esse número. (Considere que não haverão números
   repetidos no vetor).
'''

vetor = []

while True:
  num = float(input("Digite um número: "))
  vetor.append(num)

  if len(vetor) == 20:
    break

num = float(input("Digite mais um número: "))
if num in vetor:
  vetor.remove(num)
  print(f"Vetor: {vetor}")
else:
  print("Número não encontrado")