# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci

n = int(input('Quantos números você deseja ver na sequencia? '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} {t2} ', end='')
while cont <= n:
    f = t1 + t2
    t1 = t2
    t2 = f
    cont += 1
    print(f'{f} ', end='')
print('FIM')
