# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. só que agora o jogador vai tentar adivinhar até acertar , mostrando no final quantos palpites foram necessários para vencer

from random import randint

randNum = randint(0, 10)
palpites = 1
userNum = int(input('Dígite um número entre 0 e 10: '))
while userNum != randNum:
    if userNum != randNum:
        print('Você errou, continue tentando!')
        userNum = int(input('Dígite um número entre 0 e 10: '))
        palpites += 1
    else:
        print('Você dígitou um comando inválido, tente novamente!\n')
    if userNum == randNum:
        print('Parâbens, você acerou o número sorteado!')
print(f'Você precisou de {palpites} palpites para acertar o número sorteado!')
