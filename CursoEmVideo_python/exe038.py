# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

int1 = int(input('Dígite um número: '))
int2 = int((input('Dígite mais um número: ')))

if int1 > int2:
    print('O primeiro valor é maior')
elif int2 > int1:
    print('O segundo valor é maior')
else:
    print('Não tem valor maior, os dois são iguais')