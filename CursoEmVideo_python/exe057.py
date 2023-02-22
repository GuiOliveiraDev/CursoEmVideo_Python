# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto
masculino = 0
feminino = 0
sexo = ''
while sexo != 's':
    print('Para sair do programa dígite: [S] ')
    sexo = input('Qual o seu sexo? [M/F] ').lower()
    if sexo == 'm':
        masculino += 1
    elif sexo == 'f':
        feminino += 1
    elif sexo == 's':
        print('Você saiu do programa')
    else:
        print('Você dígitou um comando inválido, tente novamente!\n')
print(f'Foram registradas {masculino} pessoas do sexo masculino e, {feminino} pessoas do sexo feminino. ')
