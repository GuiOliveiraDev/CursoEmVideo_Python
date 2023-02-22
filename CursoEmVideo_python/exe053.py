# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = input('Escreva uma frase: ').lower().replace(' ', '')
invertido = ''
for i in range(len(frase) -1, -1, -1):
    invertido += frase[i]
print(f'O inverso de {frase} é {invertido}')
if frase == invertido:
    print('A frase dígitada é um palindromo')
else:
    print('A frase dígitada não é um palindromo')
