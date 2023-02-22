# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
nome = input('Dígite seu nome: ').strip()
print(f'Seu nome é: {nome.title()} ')
print(f'Seu nome tem Silva? {"silva" in nome.lower()} ')