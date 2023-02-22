#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se po acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import date
data_atual = date.today()
pessoa = {}

pessoa['nome'] = input('Nome: ')
pessoa['ano_nascimento'] = int(input('Ano de nascimento: '))
pessoa['idade'] = data_atual.year - pessoa['ano_nascimento']
pessoa['carteira_trabalho'] = int(input('Carteira de trabalho: [0 se não tiver CTPS] '))

if pessoa['carteira_trabalho'] != 0:
    pessoa['ano_contrato'] = int(input('Ano do contrato: '))
    pessoa['contribuição'] = data_atual.year - pessoa['ano_contrato']
    pessoa['salario'] = float(input('Sálario: '))
    pessoa['ano_aposentar'] = pessoa['idade'] + 15 - pessoa['contribuição']

    print('-='*30)

    if pessoa['ano_aposentar'] == pessoa['idade']:
        print('Voce ja pode se aposentar!')

    elif pessoa['ano_aposentar'] < pessoa['idade']:
        print(f'Você já poderia ter se aposentado com {pessoa["ano_aposentar"]} anos de idade')
        
    else:
        print(f'Voce devera se aposentar com {pessoa["ano_aposentar"]} anos, apos 15 anos de contribuição')
    