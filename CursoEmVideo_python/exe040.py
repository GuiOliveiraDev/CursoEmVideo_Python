# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = eval(input('Primeira nota: '))
nota2 = eval(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'Sua média foi de {media:.1f}, e você foi REPROVADO!')
elif media >= 7:
    print(f'Sua média foi de {media:.1f}, e você foi APROVADO!')
else:
    print(f'Sua média foi de {media:.1f}, e você esta em RECUPERAÇÃO!')
    