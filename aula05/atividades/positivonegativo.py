#Solicite ao usuário um valor numérico, inteiro ou real, e escrever
#se é positivo ou negativo (considere o valor zero como positivo).

num = float(input("Digite um número: "));

if num >= 0:
  print(f"{num} é positivo");
else:
  print(f"{num} é negativo");