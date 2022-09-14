#Solicite ao usuário um valor numérico, inteiro ou real, e
#verifique se ele é maior ou menor que 10. O programa deve
#escrever a mensagem correspondente (maior ou menor) e
#informar o valor digitado pelo usuário.

controle = True;

while controle:
  print('Digite 0 para sair ou outro número para continuar');
  num = float(input('Digite o número escolhido: '))

  if num == 0:
    controle = False;
  elif num > 10:
    print(f'{num} é maior que 10');
  elif num < 10 and num != 0:
    print(f'{num} é menor que 10');