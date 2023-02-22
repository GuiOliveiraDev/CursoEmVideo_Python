import math
angulo = eval(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'sendo um angulo de {angulo}°\no calculo do seno é {seno:.2f}\ndo cosseno é {cosseno:.2f}\ne a tangente é {tangente:.2f} ')