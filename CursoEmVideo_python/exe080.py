# Crie um programa onde o usúario possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort())
# No final mostre a lista ordenada na tela

valores = []
for v in range(0, 5):
    num = int(input('Dígite um valor: '))

    if v == 0 or num > valores[-1]:
        valores.append(num)
        print('O valor foi inserido no fim da Lista')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'O valor foi inserido na posição {pos} da Lista')
                break
            pos += 1
print(valores)