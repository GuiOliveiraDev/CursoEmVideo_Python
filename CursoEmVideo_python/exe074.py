# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint
randtupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for n in randtupla:
    print(f'{n}', end=' ')
#for c in range(len(randtupla)):
#    if c == 0:
#        menor = maior = randtupla[c]
#    else:
#        if randtupla[c] < menor:
#            menor = randtupla[c]
#        elif randtupla[c] > maior:
#            maior = randtupla[c]
print(f'\nO maior valor sorteado foi {max(randtupla)}')
print(f'O menor valor sorteado foi {min(randtupla)}')
