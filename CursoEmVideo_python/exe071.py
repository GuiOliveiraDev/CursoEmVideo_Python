# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) eo programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
while True:
    print('='*20, 'BANCO CEV', '='*20)
    saque = int(input('Qual valor você quer sacar? R$'))
    nota50 = int(saque/50)
    saque = saque - (nota50*50)
    nota20 = int(saque/20)
    saque = saque - (nota20*20)
    nota10 = int(saque/10)
    saque = saque -(nota10*10)
    nota1 = int(saque/1)
    saque = saque - (nota1*1)
    if nota50 > 0:
        print(f'Total de {nota50:^3} de cedulas de R$50')
    if nota20 > 0:
        print(f'Total de {nota20:^3} de cedulas de R$20')
    if nota10 > 0:
        print(f'Total de {nota10:^3} de cedulas de R$10')
    if nota1 > 0:
        print(f'TOtal de {nota1:^3} de cedulas de R$1')
    break
print('='*51)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
