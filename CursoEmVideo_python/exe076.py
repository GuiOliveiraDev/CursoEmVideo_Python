# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência
# No final, mostre uma listagem de preços, organizando os dados de forma tabular
produtos = ('computador', 2000, 'celular', 2500, 'televisao', 1500, 'sofa', 800, 'cama', 900)

print('-'*30,'LISTAGEM DE PREÇOS', '-'*30)
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<30}R${produtos[c+1]:>7.2f}')
