# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos

nomeHomemMaisVelho = ''
mulherMenos20 = 0
somaIdade = 0
idadeHomem = 0
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    somaIdade += idade
    if sexo == 'F':
        if idade < 20:
            mulherMenos20 += 1
    if sexo == 'M':
        if i == 1:
            idadeHomem = idade
        elif idade > idadeHomem:
            idadeHomem = idade
            nomeHomemMaisVelho = nome
medIdade = somaIdade / 4
print(f'A média de idade do grupo é de {medIdade}')
print(f'O homem mais velho é {nomeHomemMaisVelho}, com {idadeHomem} anos')
print(f'{mulherMenos20} mulheres tem menos de 20 anos')
