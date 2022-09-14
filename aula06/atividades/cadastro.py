'''
6. Faça um cadastro de usuários com nome, idade
e email, utilizando apenas o que você aprendeu até
agora.
'''
controle = True;

while controle:
  nome = input('Digite seu nome ou "fim" para finalizar o programa: ');

  if (nome == 'fim'):
    controle = False;
    break;

  idade = input('Digite sua idade: ');
  email = input('Digite seu e-mail: ');
  print(f'Cadastro de usuário: [nome: {nome}, idade: {idade}, e-mail: {email}]');