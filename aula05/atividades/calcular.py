#Crie um programa em Python que solicite um número do usuário,
#depois some este número com 1357, multiplique por 8, divida
#por 5 e eleve ao quadrado.

num = int(input("Digite um número, por favor: "));
resp = ((num + 1357) * 8 / 5) ** 2;
print("Resposta: {:.2f}".format(resp));