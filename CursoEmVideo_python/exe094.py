# Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas 
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média

pessoa = {}
pessoas = []
soma_idade = 0

while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['gênero'] = input('Gênero [M/F]: ').lower()[0]

    pessoas.append(pessoa.copy())
    soma_idade += pessoa['idade']

    seguir = ' '
    if seguir not in 'sn':
        seguir = input('Deseja continuar? [S/N] ')
    if seguir == 'n':
        break

média_idade = soma_idade / len(pessoas)


print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A média de idade do grupo é de {média_idade}')
print(f'As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['gênero'] == 'f':
        print(f'{p["nome"]}', end='\n')
print(f'As pessoas acima da média de idade foram ', end='')
for p in pessoas:
    if p['idade'] > média_idade:
        print(f'{p["nome"]}', end='\n')
