# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = eval(input('Qual seu peso? '))
altura = eval(input('Qual sua altura? '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'{imc:.1f} Abaixo do peso')
elif imc < 25:
    print(f'{imc:.1f} Peso ideal')
elif imc < 30:
    print(f'{imc:.1f} Acima do peso')
elif imc < 40:
    print(f'{imc:.1f} Obesidade')
else:
    print(f'{imc:.1f} Obesidade morbida')