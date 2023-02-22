# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas
# O nome com todas letras minúsculas
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome

frase = input('Digite seu nome completo: ').strip()
frase2 = frase.replace(' ', '')
frase3 = frase.split()
print(frase.upper())
print(frase.lower())
print(len(frase2))
print(len(frase3[0]))