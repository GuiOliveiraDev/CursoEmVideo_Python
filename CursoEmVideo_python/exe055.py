# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0

for i in range(1, 6):
    peso = eval(input(f'Peso da {i} pessoa: ')) 
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'O maior peso foi de {maior}!')
print(f'E o menor peso foi de {menor}!')
