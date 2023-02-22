# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = eval(input('Qual o valor do produto? R$'))

print('''\n[ 1 ]À vista no dinheiro: 10% de desconto
[ 2 ]No cartão:
À vista no cartão: 5% de desconto
Em até 2x no cartão: preço normal
Em 3x ou mais no cartão: 20% de juros''')

pagamento = int(input('\nQual a forma de pagamento? '))

if pagamento == 2:
    print('Pagamento no cartão: ')
    print('À vista [ 1 ]')
    parcela = int(input('Quantas parcelas? '))
    if parcela == 1:
        pagar = preco - preco * 0.05
        print(f'Pagamento à vista no cartão, o valor total é de R${pagar:.2f}')
    elif parcela == 2:
        print(f'Em 2x de R${preco/parcela} no cartão, o valor total é de R${preco:.2f}')
    elif parcela >= 3:
        pagar = preco + preco * 0.2
        print(f'Em {parcela}x de R${pagar/parcela:.2f} no cartão, o valor total é de R${pagar:.2f}')

elif pagamento == 1:
    pagar = preco - preco * 0.1
    print(f'Pagamento à vista em dinheiro, o valor total é R${pagar:.2f}')

else:
    print('Você escolheu uma opção invalida!')
