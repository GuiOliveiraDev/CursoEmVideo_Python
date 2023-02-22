# Desenvolva um programa que calcule a distância de uma viagem em Km, Calcule o preço da passagem, Cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

distância = eval(input('Digite a distancia da viagem em Km: '))
if distância <= 200:
    passagem = distância * 0.50
else:
    passagem = distância * 0.45
print(f'Sua viagem tem {distância}Km, e sua passagem irá custar R${passagem}')