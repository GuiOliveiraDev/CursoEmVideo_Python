# Faça um program que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

# Exemplo:
'''
nome = Ana Maria de Souza
primeiro = Ana
ultimo = Souza
'''
nome = input('Escreva seu nome completo: ').strip()
primeiro = nome.split()
ultimo = nome.split()
print(nome)
print('seu primeiro nome é: {}'.format(primeiro[0]))
print('Seu último nome é: {}'.format(ultimo[len(ultimo)-1]))
