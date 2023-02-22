# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master
import time

nasc = int(input('Qual ano você nasceu? '))
idade = time.localtime().tm_year - nasc

if idade <= 9:
    print(f'Você esta na categoria Mirim até 9 anos, voce tem {idade} anos!')
elif idade <= 14:
    print(f' Você está na categoria Infantil até 14 anos, você tem {idade} anos!')
elif idade <= 19:
    print(f'Você está na categoria Junior até 19 anos, você tem {idade} anos!')
elif idade <= 25:
    print(f'Você está na categoria Sênior até 25  anos, você tem {idade} anos!')
else:
    print(f'Você está na categoria Master acima de 20 anos, você tem {idade} anos!')
