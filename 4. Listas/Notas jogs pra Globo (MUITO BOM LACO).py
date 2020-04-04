
notas_jogadores = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]
voto = 1
qt_voto = 0

while voto != 0:
    voto = int(input('Qual seu voto? '))
    j = 0
    if voto > 0 and voto <= 10:
        qt_voto += 1
    for k in range(0, 10):
        if notas_jogadores[j] == voto:
            notas_jogadores[j + 1] += 1
        j += 2

print(notas_jogadores)
print(f'a) Foram computados {qt_voto} votos')
print('b) e c) Os jogadores votados foram:')
v = 1
print(f'Jogador | Votos    |       %')
print('-' * 30)
maior = 0
for k in range(0, 10):
    if notas_jogadores[v] != 0:
        print(f'{notas_jogadores[v - 1]}       |   {notas_jogadores[v]}      |    {(notas_jogadores[v] * 100) / qt_voto:.2f}%')
        if notas_jogadores[v] > maior:
            maior = notas_jogadores[v]
    v += 2

print('-=' * 30)
print()
g = 1
for p in range(0, 10):
    if notas_jogadores[g] == maior:
        print(f'd) O melhor jogador foi {notas_jogadores[g - 1]} com {notas_jogadores[g]} votos, correspondendo a {(notas_jogadores[g] * 100) / qt_voto:.2f}%')
    g += 2