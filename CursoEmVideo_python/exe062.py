# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos 

termo = int(input('Escreva o termo da PA: '))
razão = int(input('Escreva a razão da PA: '))
a = termo
n = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while n <= total :
        print(f'{a}')
        a += razão
        n += 1
    mais = int(input('Quantos voce quer ver mais? [digite 0 para sair]'))
print('O programa foi encerrado')
