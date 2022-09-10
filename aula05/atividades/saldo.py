#Faça um algoritmo para ler: número da conta do cliente, saldo,
#débito e crédito. Após, calcular e escrever o saldo atual
#(saldo atual = saldo - débito + crédito). Também testar se
#saldo atual for maior ou igual a zero escrever a mensagem
#'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

num = input("Digite o número da conta: ");
saldo = float(input("Saldo da conta: "));
debito = float(input("Débito da conta: "));
credito = float(input("Crétido da conta: "));

saldo = saldo - debito + credito;
print("Salto atual: {:.2f}".format(saldo));

if saldo >= 0:
  print("Sado positivo");
else:
  print("Saldo negativo");