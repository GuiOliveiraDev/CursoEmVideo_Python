# Crie um programa que vai ler vários números e colocar em uma lista, Depois disso mostre:
# A- Quantos números foram digitados
# B- A lista de valores, ordenada de forma decrescente
# C- Se o valor 5 foi digitado e está ou não na lista

lista = []
while True:
    lista.append(int(input('Dígite um valor: ')))
    seguir = ' '
    while seguir not in 'sn':
        seguir = input('Deseja continuar? [S/N]').strip().lower()[0]
    if seguir == 'n':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} números na Lista!')
print(lista)
if 5 in lista:
    print('O valor 5 foi digitado e ESTÁ na Lista!')
else:
    print('O valor 5 não foi digitado e NÃO está na Lista!')