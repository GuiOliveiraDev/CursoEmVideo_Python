# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valoraes e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
maior = menor = total = media = soma =  0
resp = 's'
while resp == 's':
    num = int(input('Dígite um número: '))
    total += 1
    soma += num
    if total == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
media = soma / total
print(f'A média dos números é de {media}, o maior valor é {maior}, e o menor valor é {menor}')
