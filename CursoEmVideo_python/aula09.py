frase = 'Curso em Vídeo Python'

#Fatiamento
'''
print(frase[9])
print(fras[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
'''
#Análise
'''
print(len(frase))
print(frase.count('C',0,13))
print(frase.find('Curso'))
print('Curso' in frase)
'''
#Transformação
'''
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase = '   Aprenda Python  '
print(frase)
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())
'''

#Divisão
'''
print(frase.split())
'''
#Junção
'''
print('-'.join(frase2))
'''
#Alteração em uma variável String com replace
'''
print(frase)
frase = frase.replace('Python', 'Android')
print(frase)
'''
#Usando split e mostrando seus índices
'''
dividido = frase.split()
print(dividido[2])
print(dividido[2][3])
'''