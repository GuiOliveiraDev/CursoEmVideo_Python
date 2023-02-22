#  Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint
from time import sleep
sorteio = []
jogos = []
cont = 1
qntjogos = int(input('Quantos jogos você quer sortear? '))
print('-='*5, f'SORTEANDO {qntjogos}', '-='*5)
while cont <= qntjogos:
    c = 0
    while True:
        num = randint(1, 61)
        if num not in sorteio:
            sorteio.append(num)
            c += 1
        if c >= 6:
            break
    sorteio.sort()
    jogos.append(sorteio[:])
    sorteio.clear()
    cont += 1
for c in range(0, len(jogos)):
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(1)