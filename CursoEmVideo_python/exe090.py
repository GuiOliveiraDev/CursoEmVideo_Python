# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

dicio = {}
dicio['nome'] = input('Nome: ')
dicio['media'] = float(input(f'Média de {dicio["nome"]}: '))
if dicio['media'] < 5:
    dicio['situação'] = 'Reprovado'
elif dicio['media'] < 7:
    dicio['situação'] = 'Recuperação'
elif dicio['media'] >= 7 :
    dicio['situação'] = 'Aprovado'
print('-='*30)
print(f'nome é igual a {dicio["nome"]}')
print(f'média é igual a {dicio["media"]}')
print(f'situação é igual a {dicio["situação"]}')
