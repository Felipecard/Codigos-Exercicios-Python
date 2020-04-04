print('Mais sobre matriz - 87')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o numero em [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

soma_pares = 0
soma_coluna_tres = 0
maior_linha_dois = []
for l in range(0, 3):
    for c in range(0, 3):
        if(matriz[l][c] % 2 == 0):
            soma_pares += matriz[l][c]
        if(l == 0 and c == 2 or l == 1 and c == 2 or l == 2 and c == 2):
            soma_coluna_tres += matriz[l][c]
        if (l == 1 and c == 0 or l == 1 and c == 1 or l == 1 and c == 2):
            maior_linha_dois.append(matriz[l][c])

print('-=' * 30)
print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_coluna_tres}')
print(f'O maior valor da segunda linha é: {max(maior_linha_dois)}')

#OUTRO MODO DE RESOLVER A SEGUNDA E A TERCEIRA PERGUNTA
#for l in range(0, 3):
    #soma_coluna_tres += matriz[l][c]
#print(soma_coluna_tres)