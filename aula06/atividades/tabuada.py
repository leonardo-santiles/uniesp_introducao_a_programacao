'''
4. Faça um programa que receba um número
e que calcule e mostre a tabuada desse número.
'''

num = int(input("Digite um número, por favor: "));

print(f'Tabuada do {num} \n');

for i in range(1, 11):
    print(f'{num} x {i} = {i * num}');