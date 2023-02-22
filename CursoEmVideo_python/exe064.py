# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usúario digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsidreando o flag)
digitados = n = soma = 0
while n != 999:
    n = int(input('Dígite um número [999 para encerrar]:  '))
    if n == 999:
        print('O programa foi encerrado! ')
    else:
        soma += n
        digitados += 1
print(f'Foram dígitados {digitados} números, e a soma entre eles é de {soma}')