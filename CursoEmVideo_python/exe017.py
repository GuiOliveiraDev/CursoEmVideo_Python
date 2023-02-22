import math
catOposto = eval(input('Digite o comprimento do cateto oposto'))
catAdjacente = eval(input('Digite o comprimento do cateto adjacente'))
print(f'O comprimento da hipotenusa de um triângulo retangulo, de cateto oposto = {catOposto} e de cateto adjacente = {catAdjacente} é = {math.hypot(catOposto,catAdjacente):.5f} ')