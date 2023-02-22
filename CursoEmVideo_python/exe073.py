# Crie um tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time da chapecoense

tabelaTimes = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico PR', 'Atletico Mineiro', 'Fortaleza', 'Sao Paulo', 'America MG', 'Botafogo', 'Santos', 'Goias', 'RedBull Brasil', 'Coritiba', 'Cuiaba', 'Ceara', 'Atletico GO', 'Avai', 'Juventude')

print('-='*30)
print(f'lista de times do Brasileirão: {tabelaTimes}')

print('-='*30)
print(f'Os 5 primeiros colocados do Brasileirão são: {tabelaTimes[0:5]}')

print('-='*30)
print(f'Os 4 últimos são: {tabelaTimes[-4:]}')

print('-='*30)
print(f'Times em ordem alfabética: {sorted(tabelaTimes)}')

print('-='*30)
print('A chapecoense se encontra na Série B do campeonato Brasileiro, na 14º Pósição!')
print('-='*30)
