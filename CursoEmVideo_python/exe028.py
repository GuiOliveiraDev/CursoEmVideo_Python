# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

#O programa devera escrever na tela se o usuário ganhou ou perdeu!
 
from random import randint

# sortea um número
randNum = randint(0, 5)

# O usúario tenta adivinhar o número sorteado
userNum = int(input('Dígite um número entre 0 e 5: '))  

print(f'O número que você dígitou foi {userNum}')

print(f'O número sorteado foi: {randNum}')

if userNum == randNum:
    print('Você ganhou!')
else:
    print('Você perdeu!')