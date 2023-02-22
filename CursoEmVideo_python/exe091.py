# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint

resultados = {}

for i in range(0, 4):
    jogador = randint(1, 7)
    resultados[f'jogador{i+1}'] = jogador
for k, v in resultados.items():
    print(f'{k} tirou {v} no dado')

print(resultados)