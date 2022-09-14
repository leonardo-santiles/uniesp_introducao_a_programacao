'''
2. Faça um programa que mostre as
tabuadas dos números de 1 a 10.
'''

for num in range(1, 11):
    print(f'Tabuada do {num} \n');

    for num2 in range(1, 11):
        print(f'{num} x {num2} = {num * num2}');

    print('----------------');