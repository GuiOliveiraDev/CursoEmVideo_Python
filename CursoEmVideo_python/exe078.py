# Faça um programa que leia 5 valores nuḿericos e guarde os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

valores = []
for cont in range(0, 5):
    valores.append(int(input('Dígite um número: ')))
for p, v in enumerate(valores):
    if p == 0:
        maior = menor = v
        posmenor = posmaior = p
    else:
        if v < menor:
            menor = v
            posmenor = p
        elif v > maior:
            maior = v
            posmaior = p
print(f'O maior valor dígitado foi {maior}, na posição {posmaior}')
print(f'O menor valor dígitado foi {menor}, na posição {posmenor}')
