# Faça um programa que leia uma frase pelo teclado e mostre:

# Quantas vezes aparece a letra "a"
# Em que posição ela aparece a primeira vez
#Em que posição ela aparece a ultima vez

frase = input('Escreva uma frase: ').strip().lower()

print('A letra "a" aparece {} vezes na frase!'.format(frase.lower().count('a')))
print('A letra "a" aparece pela primeira vez na posição {}!'.format(frase.lower().find('a')+1))
print('A letra "a" aparece pela última vez na posição {}!'.format(frase.lower().rfind('a')+1))