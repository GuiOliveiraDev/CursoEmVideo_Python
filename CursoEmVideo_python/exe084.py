# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista, no final mostre:
# A- Quantas pessoas foram cadastradas
# B- Uma listagem com as pessoas mais pesadas
# C- Uma listagem com as pessoas mais leves

pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    seguir = ' '
    while seguir not in 'sn':
        seguir = input('Deseja continuar? [S/N] ').strip().lower()[0]
    if seguir == 'n':
        break
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas.')
print(f'O menor peso foi de {menor}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print(f'\nO maior peso foi de {maior}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')