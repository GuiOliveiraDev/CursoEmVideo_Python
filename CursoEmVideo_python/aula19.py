pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
    }
# print(pessoas[0]) /// ERRO

# print(pessoas['nome']) /// pessoas['idade']

#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') /// usar ASPAS DUPLAS, QUANDO estiver entre ASPAS SIMPLES para declarar os elementos

# print(pessoas.items()) /// mostra TODOS ITENS de um dicionario

# print(pessoas.keys()) /// mostra as CHAVES de um dicionario

# Mostra os valores dentro de um dicionario:
# print(pessoas.values()) 

# Laço para percorrer todas as chaves e valores dentro de um dicionario:

# for k, v in pessoas.items():
#     print(f'{k} = {v}') 

# del pessoas['sexo'] /// para deletar um item dentro de um dicionario

# pessoas['nome'] = 'Leandro' /// para trocar valores dentro de um dicionario

# pessoas['peso'] = 98.5 /// adiciona itens dentro de um dicionario

# Usando dicionarios dentro de listas:

#brasil = []
#estado1 = {
#    'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {
#    'UF': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)

#print(brasil[1]['sigla']) /// do elemento no index 1 da lista "brasil", mostra o valor da chave "sigla" = SP 

#estado = {}
#brasil = []
#for c in range(0, 3):
#    estado['uf'] = input('Unidade federativa: ')
#    estado['sigla'] = input('Sigla do Estado: ')
#    brasil.append(estado.copy())
#for e in brasil:
#    for v in e.values():
#        print(v)