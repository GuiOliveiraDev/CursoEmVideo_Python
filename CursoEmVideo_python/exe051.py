# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
print('=-'*10)
print('DEZ TERMOS DE UMA PA')
print('=-'*10)
termo = int(input('Escreva o termo da PA: '))
razão = int(input('Escreva a razão da PA: '))
for i in range(0 ,10):
    a = termo + i * razão
    print(a, end=' ')
