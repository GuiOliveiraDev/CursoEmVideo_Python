wallLength = eval(input('Qual o comprimento da parede? '))
wallHeight = eval(input('Qual a altura da parade? '))
wallArea = wallLength * wallHeight
paintYield = 2
paintNeeded = wallArea / paintYield
print(f'Voce precisará de {paintNeeded:.3} Litros de tinta, para pintar sua parede!')