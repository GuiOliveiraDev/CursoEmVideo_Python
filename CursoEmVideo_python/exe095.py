# Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

status_jogador = {}
jogadores = []
while True:

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

    jogadores.append(status_jogador.copy())

    seguir = ' '
    while seguir not in 'sn':
        seguir = input('Deseja continuar? [S/N] ').lower()[0]
    if seguir == 'n':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<15}{"GOLS":<15} {"TOTAL":<6}')
print('-'*60)

for j, v in enumerate(jogadores):

    print(f'{j:<4}{v["nome"]:<15}{list(v["gols"].values())} {v["total_gols"]:>6}')

while True:
    mostrar = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if mostrar == 999:
        break
    if mostrar > len(jogadores) :
        print('Não existente!')
    elif mostrar <= len(jogadores):
        print(f'Levantamento do jogador {jogadores[mostrar]}')