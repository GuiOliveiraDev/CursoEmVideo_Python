# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

houseValue = eval(input('Qual o valor da casa? '))
salary = eval(input('Qual o seu salário? '))
yearsPay = eval(input('Quantos anos você pretende ficar pagando? ')) 
parcela = houseValue / (yearsPay * 12)

if parcela > salary * 0.3:
    print('O emprestimo foi negado, pois a parcela ultrapassa 30% do seu salário')
    print(f'O valor da parcela mensal é de R${parcela:.2f}')
else:
    print('Seu empréstimo foi concedido!')
    print(f'O valor da parcela mensal é de R${parcela:.2f}')