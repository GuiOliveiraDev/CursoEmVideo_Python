# Crie um programa que leia a idade eo sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# Quantas pessoas tem mais de 18 anos
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos

mais18 = homem = mulherMenos20 = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Qual seu sexo? [M/F] ')).lower().strip()[0]
    if idade >= 18:
        mais18 += 1
    if sexo == 'm':
        homem += 1
    elif sexo == 'f' and idade < 20:
        mulherMenos20 += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Cadastro concluido. Deseja continuar? [S/N] ')).lower().strip()[0]
    if continuar == 'n':
        break
print('-'*10,'FIM DO PROGRAMA','-'*10)
print(f'Total de pessoas com mais de 18 anos : {mais18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulherMenos20} mulheres com menos de 20 anos')
print('ACABOU')