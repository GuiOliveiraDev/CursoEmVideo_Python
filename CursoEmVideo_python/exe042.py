# Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

num1 = eval(input('Primeiro segmento: '))
num2 = eval(input('Segundo segmento: '))
num3 = eval(input('Terceiro segmento: '))
if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
    print(f'Forma um triângulo!')

    if num1 == num2 and num2 == num3:
        print('E é um triângulo Equilátero!')
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print('E é um triângulo Isósceles!')
    else:
        print('E é um triângulo Escaleno!')
        
else:
    triangulo = False
    print('Não forma um triângulo!')
