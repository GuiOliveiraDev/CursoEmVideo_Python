# Crie um programa que o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado
# No final, serão exibidos todos os valores unicos digitados, em ordem crescente

valores = []
while True:
    num = int(input('Dígite um valor: '))
    if num in valores:
        print('Valor não adicionado! O valor dígitado já existe na Lista!')
    else:
        valores.append(num)    
    seguir = input('Deseja continuar? [S/N] ').strip().lower()[0]
    while seguir not in 'sn':
        seguir = input('Deseja continuar? [S/N] ').strip().lower()[0]
    if seguir == 'n':
        break
valores.sort()
print(valores)