# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
# Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por exenso

numExt = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    seguir = ' '
    numero = int(input('Dígite um número [entre 0 e 20]: '))
    if numero < 0 or numero > 20:
        print('Dígite um número válido!')
    else:
        print(f'Você dígitou o número {numExt[numero].capitalize()}')
    while seguir not in 'ns':
        seguir = input('Você quer continuar? [S/N] ').strip().lower()[0]
    if seguir == 'n':
        break
    
