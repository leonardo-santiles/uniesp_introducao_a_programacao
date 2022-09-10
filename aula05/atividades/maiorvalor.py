#Ler dois valores (considere que não serão lidos valores iguais)
#e escreva o maior deles.

num1 = float(input("Digite o 1º número: "));
num2 = float(input("Digite o 2º número: "));

if num1 > num2:
  print(f"{num1} é o maior");
else:
  print(f"{num2} é o maior")