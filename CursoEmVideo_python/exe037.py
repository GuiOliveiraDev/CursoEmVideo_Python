# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 para bínario
# 2 para octal
# 3 para hexadecimal

inteiro = eval(input('Dígite um número: '))
fazer = int(input('Dígite 1 para converter para Bínario\nDígite 2 para converter em Octal\nDígite 3 para converter em Hexadecimal\n'))

if fazer == 1:
    print(f'{inteiro} convertido para Bínario fica {bin(inteiro)[2:]}')
elif fazer == 2:
    print(f'{inteiro} convertido para Octal fica {oct(inteiro)[2:]}')
elif fazer == 3:
    print(f'{inteiro} convertido para Hexadecimal fica {hex(inteiro)[2:]}')
else:
    print('Você digitou um número inválido, dígite um número válido')