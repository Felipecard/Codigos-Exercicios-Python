#Exercicio 19
lista_candi = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
voto = 1
nomes = ['Windows', 'Unix', 'Linux', 'Netware', 'Mac', 'Outro']
qt_votos = 0
print('Os sistemas operacionais candidatos:')
print('1 - Windows | 2 - Unix | 3 - Linux | 4 - Netware | 5 - Mac | 6 - Outro')
print('-=' * 30)

while voto != 0:
    voto = int(input('Qual o voto? '))
    if voto != 0:
        qt_votos += 1
    j = 0
    for k in range(0, 6):
        if lista_candi[j] == voto:
            lista_candi[j + 1] += 1
        j += 2

print(lista_candi)
o = 1
l = 0
p = 0
cont = 0
print(f'{"Sistema Operacional":<5}{"Votos":>10}{"%":>10}')
print('-' * 50)
for k in range(0, 6):
    if lista_candi[o] != 0:
            print(f'{nomes[p]:<5}{lista_candi[o]:>22}{(lista_candi[o] * 100) / qt_votos:>15.2f} %' )
            cont += 1
    o += 2
    p += 1
    l += 2
print('-' * 50)
print(f'TOTAL: {qt_votos:>20}')
print()
r = 1
maior = 0
for k in range(0, 6):
    if lista_candi[r] > maior:
        maior = lista_candi[r]
    r += 2

h = 0
q = 1
for k in range(0, 6):
    if lista_candi[q] == maior:
        print(f'O sistema operacional mais votado foi o {nomes[h]}, com {(lista_candi[q] * 100) / qt_votos:.2f} % dos votos')
    q += 2
    h += 1

