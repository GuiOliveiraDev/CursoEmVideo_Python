# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input('Escreva o nome de uma cidade: ').strip()
print(f'Sua cidade é:{cidade.title()} ')
print(cidade[:5].upper() == 'SANTO') 