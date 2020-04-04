
def ficha(jogador='', gol=''):
    if jogador == '':
        jogador = '<Desconhecido>'
    if gol == '':
        gol = 0
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')




jog = str(input('Nome do jogador: '))
g = str(input('Numero de Gols: '))
ficha(jog, g)