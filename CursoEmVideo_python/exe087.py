# Aprimore o desafio anterior, mostrando no final
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna
# C) O maior valor da segunda linha

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = 0
somaTerCol = 0
maiorSeglin = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Dígite um valor para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2 :
            somaTerCol += matriz[l][c]
        if l == 1:
            maiorSeglin = matriz[1][c]
        if matriz[1][c] > maiorSeglin:
            maiorSeglin = matriz[1][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print('\n')
print(f'A soma de todos os valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somaTerCol}')
print(f'O maior valor da segunda linha é {maiorSeglin}')
