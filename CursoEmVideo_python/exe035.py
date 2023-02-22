# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

num1 = eval(input('Primeiro segmento: '))
num2 = eval(input('Segundo segmento: '))
num3 = eval(input('Terceiro segmento: '))

if num1 + num2 > num3 and num1 + num3 > num2 and num3 + num2 > num1 :
    print('é um triangulo!')
else:
    print('Não forma um triangulo!')