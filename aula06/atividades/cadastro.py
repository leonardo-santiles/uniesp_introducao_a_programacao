'''
7. Faça um cadastro de usuários com nome, idade
e email, utilizando apenas o que você aprendeu até
agora.
'''
usuarios = [];
botao = 1000;

while botao != 0:
  print("Digite 0 para sair");
  print("Digite 1 para cadastrar novo usuário");
  print("Digite 2 para imprimir todos os usuários");

  botao = int(input("Digite a opção desejada: "));

  if botao == 1:
    nome = input("Digite o nome: ");
    idade = int(input("Digite a idade: "));
    email = input("Digite o e-mail: ");

    usuario = [nome, idade, email];
    usuarios.append(usuario);

  elif botao == 2:
    for usuario in usuarios:
      print(usuario);

  elif botao == 0:
    print("Obrigado por utilizar o app!");

  else:
    print("Digite uma opção válida");