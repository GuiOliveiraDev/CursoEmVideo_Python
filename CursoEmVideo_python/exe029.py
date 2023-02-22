# Escreva um programa que leia a velocidade de um carro

# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado 

#A multa vai custar R$7,00 por cada Km acima do limite

carSpeed = int(input('Qual foi a sua velocidade? '))
if carSpeed > 80:
    excesso = carSpeed - 80
    multa = excesso * 7
    print(f'Você foi multado por ultrapassar a velocidade máxima estabelecida de, 80Km/h.\nO valor da sua multa é de: R${multa}!')
else:
    print('Tenha um bom dia! Dirija com segurânça!')