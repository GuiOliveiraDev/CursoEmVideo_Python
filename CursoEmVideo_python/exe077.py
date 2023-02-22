# Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais

palavras = ('passaro', 'escola', 'praca', 'violao', 'sol', 'lua', 'futebol', 'esporte', 'programacao', 'trabalho')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')