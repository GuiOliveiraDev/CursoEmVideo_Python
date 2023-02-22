# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidadde de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

status_jogador = {}

nome_jogador = input('Nome do jogador: ')
jogos = int(input('Partidas jogadas: '))

gols = {}
for i in range(jogos):
    gol = int(input(f'Gols marcados na partida {i+1}: '))
    gols[f'partida{i+1}'] = gol

status_jogador['nome'] = nome_jogador
status_jogador['jogos'] = jogos
status_jogador['gols'] = gols
status_jogador['total_gols'] = sum(gols.values())

print(status_jogador)