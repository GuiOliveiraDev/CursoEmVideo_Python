# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares, no final, moste os valores pares e ímpares em ordem crescente

princ = [[],[]]
temp = 0
for c in range(1, 8):
    temp = int(input(f'Digite o {c}º valor: '))
    if temp % 2 == 0:
        princ[0].append(temp)
    else:
        princ[1].append(temp)
princ[0].sort()
princ[1].sort()
print(f'Os valores pares foram {princ[0]}')
print(f'Os valores ímpares foram {princ[1]}')
