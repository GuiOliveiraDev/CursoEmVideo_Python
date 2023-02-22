# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor

num1 = int(input('Dígite seu 1 número: '))
num2 = int(input('Dígite seu 2 número: '))
num3 = int(input('Dígite seu 3 número: '))
maior = num1
menor = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
print(f'O maior número é {maior}!')

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
print(f'O menor número é {menor}')