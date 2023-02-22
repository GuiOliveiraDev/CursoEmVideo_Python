# Faça um progrma que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo de alistamento

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

import time
anoNasci = int(input('Ano de nascimento: '))
idade = time.localtime().tm_year - anoNasci
print(idade)
if idade == 18:
    print(f'você tem {idade} anos, e é hora de se alistar no exército')
elif idade < 18:
    print(f'você tem {idade} anos, não está na hora de vocẽ se alistar ainda. Faltam {18-idade} anos para você se alistar!')
elif idade > 18:
    print(f'Você tem {idade} anos, você está {idade-18} anos atrásado para se alistar!')