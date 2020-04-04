from random import randint
from time import sleep

print('-' * 30)
print('    MEGA SENA  88    ')
print('-' * 30)


cada_jogo = []
qt_jogos = int(input('Quantos jogos voce quer que eu sorteie? '))

print('-=' * 3, f'SORTEANDO {qt_jogos} JOGOS', '-=' * 3)
for jog in range(0, qt_jogos):
    for cont in range(0, 6):
        jogo = randint(1, 60)
        while(jogo in cada_jogo):
            jogo = randint(1, 60)
        cada_jogo.append(jogo)
    print(f' Jogo {jog + 1}: {cada_jogo[:]}')
    cada_jogo.clear()
    sleep(1)

print('-=' * 3, '   BOA SPRTE    ', '-=' * 3)


