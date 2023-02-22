# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

termo = int(input('Escreva o termo da PA: '))
razão = int(input('Escreva a razão da PA: '))
n = 0
a = 0
while n < 10:
    a = a + razão
    n += 1
    print(a)
