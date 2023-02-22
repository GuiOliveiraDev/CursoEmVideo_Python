# Crie um programa que leia dois valores e mostre um menu na tela:
#[1]somar
#[2]multiplicar
#[3]maior
#[4]novos números
#[5]sair do programa
menu = 0
soma = 0
multi = 0
maior = 0
print('Dígite dois valores: \n')
n1 = int(input('Dígite um valor: '))
n2 = int(input('Dígite mais um valor: '))
while menu != 5:
    menu = int(input('''Escolha uma opção do Menu: 
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números 
    [5]sair do programa\n'''))
    if menu == 1:
        soma = n1 + n2
        print(f'A soma entre dois valores é {soma}\n')
    elif menu == 2:
        multi = n1 * n2
        print(f'A multiplicão entre os dois valores foi de {multi}\n')
    elif menu == 3:
        if n1 > n2:
            maior == n1
            print(f'O maior valor dígitado foi {maior}\n')
        elif n2 > n1:
            maior == n2
            print(f'O maior valor dígitado foi {maior}\n')
        else:
            print('Os dois valores são iguais!\n')
    elif menu == 4:
        n1 = int(input('Dígite um novo valor: '))
        n2 = int(input('Dígite mais um novo valor: '))
    elif menu == 5:
        print('Fim do programa!', end=' ')
    else:
        print('Você digitou um comando inválido, tente novamente')
print('Volte sempre!')
