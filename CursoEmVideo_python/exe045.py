# Crie um programa que faça o computador jogar Jokenpô com você
import random

jog = input('Escolha Pedra, Papel ou Tesoura: ').strip().lower()
comp = random.choice(['pedra', 'papel', 'tesoura'])
print(f'Você escolheu: {jog.title()}\nComputador escolheu: {comp.title()}')

if jog == 'pedra' and comp == 'papel':
    print('Pedra X Papel = Papel')
    print('Você Perdeu!')

elif jog == 'papel' and comp == 'pedra':
    print('Papel X Pedra = Papel')
    print('Parabêns, você ganhou!')

elif jog == 'tesoura' and comp == 'pedra':
    print('Tesoura X Pedra = Pedra')
    print('Você perdeu!')
elif jog == 'pedra' and comp == 'tesoura':
    print('Pedra X Tesoura = Pedra')
    print('Parabêns, você ganhou!')

elif jog == 'tesoura' and comp == 'papel':
    print('Tesoura X Papel = Tesoura')
    print('Parabêns, você ganhou!')

elif jog == 'papel' and comp == 'tesoura':
    print('Papel x Tesoura = Tesoura')
    print('Você perdeu!')

else:
    print(f'{jog.title()} X {comp.title()} = Empate')