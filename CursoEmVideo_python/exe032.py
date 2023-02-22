# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
from datetime import date
ano = int(input('Dígite um ano, ou dígite 0 para o ver o ano ATUAL: '))
if ano == 0:
    ano = date.today().year   
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano}, FOI um ano bissexto!')
else:
    print(f'O ano de {ano}, NÃO é um ano bissexto!')
