 # Crie um programa que vai ler vários números e colocar em uma lista, Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares dígitados, respectivamente
 # Ao final, mostre o conteúdo das três listas geradas

lista = []
pares = []
impares = []
while True:
    seguir = ' '
    lista.append(int(input('Dígite um valor: ')))
    while seguir not in 'sn':
        seguir = input('Deseja continuar? [S/N]').strip().lower()[0]
    if seguir == 'n':
        break
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    elif c % 2 == 1:
        impares.append(c)
print(lista)
print(pares)
print(impares)