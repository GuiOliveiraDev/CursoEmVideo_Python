# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares


tupla = (int(input('Dígite um valor: ')), int(input('Dígite um valor: ')), int(input('Dígite um valor: ')), int(input('Dígite um valor: ')))
print(f'Você dígitou os valores {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes!')
if 3 in tupla:
    print(f'O primeiro número 3, está na {tupla.index(3)}ª posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')
print('Os valores pares dígitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
