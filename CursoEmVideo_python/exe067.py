# Faça um programa que mostre a tabuada de vário números, um de cada vez, para cada valor dígitado pelo usuário. O programa será interrompido quando o número solicitado for NEGATIVO

while True:
    print('-'*20)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    if n < 0:
        break
    for c in range(1, 11):
        r = n * c
        print(f'{n} X {c} = {r}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')