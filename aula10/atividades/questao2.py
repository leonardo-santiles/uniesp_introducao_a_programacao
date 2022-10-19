'''
2. Escreva um algoritmo que permita a leitura das
   notas de uma turma de 20 alunos. Calcular a média
   da turma e contar quantos alunos obtiveram nota
   acima desta média calculada. Escrever a média da
   turma e o resultado da contagem.
'''

notas = []
soma = 0

while True:
  nota = float(input("Digite a nota do aluno: "))
  soma += nota
  notas.append(nota)

  if len(notas) == 20:
    break

media = soma / len(notas)
print(f"Média: {media:.2f}")

notas_acima_da_media = 0
for nota in notas:
  if nota > media:
    notas_acima_da_media += 1

print(f"Notas acima da média: {notas_acima_da_media}")