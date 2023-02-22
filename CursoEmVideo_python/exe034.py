# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

# Para salários superiores a R$1.250,00, calcule um aumento de 10%

# Para inferiores ou iguais, o aumento é de 15%

salario = eval(input('Qual o seu salário? R$'))
if salario <= 1250:
    salario = salario + salario * 0.15
    print(f'Seu salário com aumento de 15% ficou em R${salario}')
else:
    salario = salario + salario * 0.10
    print(f'Seu salário com aumento de 10% ficou em R${salario:.2f}')