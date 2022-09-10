#Solicite ao usuário um valor numérico, inteiro ou real, e
#verifique se ele é maior ou menor que 10. O programa deve
#escrever a mensagem correspondente (maior ou menor) e
#informar o valor digitado pelo usuário.

num = float(input("Digite um número: "));

if num > 10:
  print(f"{num} é maior que 10");
elif num == 10:
  print(f"{num} é igual a 10");
else:
  print(f"{num} é menor que 10");