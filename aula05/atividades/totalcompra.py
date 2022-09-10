#As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00
#se forem compradas pelo menos 12. Escreva um programa que leia o número
#de maçãs compradas, calcule e escreva o custo total da compra.

num = int(input("Digite o número de maçãs compradas: "));

if num < 12:
  print("Custo total da compra: {:.2f}".format(1.3 * num));
else:
  print("Custo total da compra: {:.2f}".format(num));