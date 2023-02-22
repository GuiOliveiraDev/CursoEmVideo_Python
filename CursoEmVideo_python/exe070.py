# Crie um programa que leia o nome eo preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$1000
# Qual é o nome do produto mais barato

total = mais1000 = cont = menor = 0
produtoBarato = ''
while True:
    nome = str(input('Nome do produto: ')).lower().strip()
    preco = eval(input('Preço: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        mais1000 += 1
    if cont == 1 or preco < menor:
        produtoBarato = nome
        menor = preco
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N]')).lower().strip()[0]
    if continuar == 'n':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O valor total da compra foi R${total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produtoBarato} que custa R${menor}')
