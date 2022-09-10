#Ler dois valores (considere que não serão lidos valores iguais)
#e escrevê-los em ordem crescente.

num1 = float(input("Digite o 1º número: "));
num2 = float(input("Digite o 2º número: "));

if num1 > num2:
  print(f"Ordem crescente: {num2}, {num1}");
else:
  print(f"Ordem crescente: {num1}, {num2}")