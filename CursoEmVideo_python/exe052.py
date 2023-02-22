# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Dígite um número: '))
cont = 0
for i in range(1, num+1):
    if num % i  != 0:
        print(f'\033[31m {i}', end=' ' )
    elif num % i == 0:
        cont += 1
        print(f'\033[33m {i}',end=' ' '\033[0;0m')

print(f'\nO número {num} foi divisível {cont} vezes')

if cont == 2:
    print('E por isso Ele É PRIMO!')
else:
    print('E por isso Ele NÃO É PRIMO!')
