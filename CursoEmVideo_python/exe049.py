# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

multiplo = int(input('Você quer ver a tabuada de qual número? '))
for i in range(0, 11):
    print(f'{multiplo} x {i} = {multiplo * i} ')