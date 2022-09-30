# Introdução à Programação
# Atividade Avaliativa
# Leonardo Santiles Dalacqua

'''
1. Construa um algoritmo para calcular as raízes de
   uma equação do 2 grau (Ax² + Bx + C), sendo que
   os valores A, B, C são fornecidos pelo usuário.
   (considere que a equação possui duas raízes reais).
'''

import math;

a = float(input("Digite o valor de A: "));
b = float(input("Digite o valor de B: "));
c = float(input("Digite o valor de C: "));

delta = math.pow(b, 2) - (4 * a * c);

if delta > 0 :
  x1 = (- b + math.sqrt(delta)) / (2 * a);
  x2 = (- b - math.sqrt(delta)) / (2 * a);
  print(f"x1: {x1:.2f}");
  print(f"x2: {x2:.2f}");
  print(f"Delta: {delta:.2f}");
else:
  print("Reduza os valores de A e C!");



'''
2. Construa um algoritmo que, tendo como dados de
   entrada dois pontos quaisquer do plano, P(x1, y1)
   e Q(x2, y2), imprima a distância entre eles.
'''

import math;

x1 = float(input("Digite o valor de x1: "));
y1 = float(input("Digite o valor de y1: "));
x2 = float(input("Digite o valor de x2: "));
y2 = float(input("Digite o valor de y2: "));

distancia = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print(f"Distância entre os pontos: {distancia:.2f}");



'''
3. Elabore um algoritmo que leia o valor de dois números
   inteiros e a operacão aritimética desejada. Calcule,
   então, a resposta adequada. Utilize os símbolos da tabela
   a seguir para ler qual operacão aritmética escolhida:
   
   Símbolo    |  Operação aritmética
       +      |       Adição
       -      |      Subtração
       *      |    Multiplicação
       /      |       Divisão
       **     |     Potenciação
'''

num1 = int(input("Digite um número: "));
num2 = int(input("Digite outro número: "));

print("Símbolo    |  Operação aritmética")
print("    +      |       Adição");
print("    -      |      Subtração");
print("    *      |    Multiplicação");
print("    /      |       Divisão");
print("    **     |     Potenciação");
opcao = input("Digite o símbolo da operação desejada: ");

if opcao == "+":
  print(f"{num1} + {num2} = {num1 + num2}");
elif opcao == "-":
  print(f"{num1} - {num2} = {num1 - num2}");
elif opcao == "*":
  print(f"{num1} * {num2} = {num1 * num2}");
elif opcao == "/":
  print(f"{num1} / {num2} = {num1 / num2}");
elif opcao == "**":
  print(f"{num1} ** {num2} = {num1 ** num2}");
else:
  print("Opção inválida!");



'''
4. O IMC - Índice de Massa Corporal - é um critério da
   Organização Mundial da Saúde para indicar a condição de
   peso de uma pessoa. A fórmula é IMC = peso / (altura)².
   Elabore um algoritmo que leia o peso e a altura de um
   adulto e mostre sua condição.

   IMC em adultos    |     Condição
   abaixo de 18,5    |  abaixo do peso
   entre 18,5 e 25   |   peso normal
      25 e 30        |  acima do peso
    acima de 30      |      obeso

'''

import math;

peso = float(input("Digite seu peso (Kg): "));
altura = float(input("Digite sua altura (m): "));

imc = peso / math.pow(altura, 2);

if imc < 18.5:
  print("Abaixo do peso");
elif imc >= 18.5 and imc < 25:
  print("Peso normal")
elif imc >= 25 and imc < 30:
  print("Acima do peso");
elif imc > 30:
  print("Obeso");



'''
5. Escrever um algoritmo que leia uma quantidade desconhecida
   de números e conte quantos deles estão nos seguintes intervalos:
   [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve
   terminar quando for lido um número negativo.
'''

num = 1;
intervalo1 = 0;
intervalo2 = 0;
intervalo3 = 0;
intervalo4 = 0;

while num > 0:
  num = int(input("Digite um número: "));

  if num >= 0 and num <= 25:
    intervalo1 = intervalo1 + 1;
  elif num >= 26 and num <= 50:
    intervalo2 = intervalo2 + 1;
  elif num >= 51 and num <= 75:
    intervalo3 = intervalo3 + 1;
  elif num >= 76 and num <= 100:
    intervalo4 = intervalo4 + 1;

print("Quantidade de números entre 00 e 25: ", intervalo1);
print("Quantidade de números entre 26 e 50: ", intervalo2);
print("Quantidade de números entre 51 e 75: ", intervalo3);
print("Quantidade de números entre 76 e 100: ", intervalo4);



'''
6. Escreva um algoritmo que leia um valor inicial A e imprima
   a sequência de valores do cálculo de A! e o seu resultado.
   Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
'''

num = int(input("Digite um número inteiro: "));
contador = 1;
fatorial = 1;

while contador <= num:
  fatorial = fatorial * contador;
  contador = contador + 1;

print(f"{num}! = {fatorial}");