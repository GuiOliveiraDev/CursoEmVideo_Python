# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

import datetime
ano = datetime.date.today().year
menor = 0
maior = 0
for i in range(1, 8):
    nasc = int(input('Qual sua ano de nascimento? '))
    idade = ano - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas atingiram a maioridade!')
print(f'{menor} pessoas NÃO ATINGIRAM a maioridade')
