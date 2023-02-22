par = 0 
impar = 0
n = 1
while n != 0:
    n = int(input('Dígite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você dígitou {par} números pares e {impar} números ímpares!')

'''c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')'''

'''n = 1
while n != 0:
    n = int(input('Dígite um valor:'))
print('Fim')'''
