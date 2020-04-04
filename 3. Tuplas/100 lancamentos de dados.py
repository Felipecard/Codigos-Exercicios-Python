from random import randint
from time import sleep

lancamentos = 100
lista_n = []
for k in range(0, lancamentos):
    n = randint(1, 6)
    lista_n.append(n)
print(lista_n)

o = 0
um = 0
dois = 0
tres = 0
quatro = 0
cinco = 0
seis = 0
for k in range(0, lancamentos):
    if lista_n[o] == 1:
        um += 1
    if lista_n[o] == 2:
        dois += 1
    if lista_n[o] == 3:
        tres += 1
    if lista_n[o] == 4:
        quatro += 1
    if lista_n[o] == 5:
        cinco += 1
    if lista_n[o] == 6:
        seis += 1
    o += 1

print('-=' * 30)
print()
print(f'O valor (1) apareceu {um} vezes')
sleep(0.5)
print(f'O valor (2) apareceu {dois} vezes')
sleep(0.5)
print(f'O valor (3) apareceu {tres} vezes')
sleep(0.5)
print(f'O valor (4) apareceu {quatro} vezes')
sleep(0.5)
print(f'O valor (5) apareceu {cinco} vezes')
sleep(0.5)
print(f'O valor (6) apareceu {seis} vezes')