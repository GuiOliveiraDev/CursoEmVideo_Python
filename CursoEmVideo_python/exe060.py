# Faça um programa que leia um número qualquer e mostre o seu fatorial

num = int(input('Dígite um valor: '))
cont = 1
resultado = 1
while cont <= num:
    resultado *= cont
    cont += 1
print(resultado)
