# Faça um programa que jogue par ou impar com o computador. O jogo só sera interrompido quando o jogador perder, mostrando o toral de vitórias consecutivas que ele conquistou no final do jogo

from random import randint
total = 0
while True:
    soma = 0
    comp = randint(1, 2)
    print('=-'*20)
    print('Vamos jogar par ou impar')
    print('=-'*20)
    user = int(input('Escolha o número 2 ou 1: '))
    while user > 2 or user < 1:
        print('Escolha um valor válido!')
        user = int(input('Escolha o número 2 ou 1: '))
    soma = user + comp
    parOuImpar = ' '
    while parOuImpar not in 'pi':
        parOuImpar = str(input('Par ou impar? [P/I] ')).lower().split()[0]
    print(f'Você jogou {user} e o computador {comp}. Total de {soma}', end= ' ')
    print('Deu PAR' if soma % 2 == 0 else 'Deu IMPAR')
    if parOuImpar == 'p':
        if soma % 2 == 0:
            print('Você GANHOU')
            total += 1
        else:
            print('Você PERDEU!')
            break
    elif parOuImpar == 'i':
        if soma % 2 == 1:
            print('Você GANHOU')
            total += 1
        else:
            print('Você PERDEU!')
        break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Você venceu {total} vezes!')
print('Fim do jogo')