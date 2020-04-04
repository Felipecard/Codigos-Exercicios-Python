
def conversao(h, m):
    hora_nova = h - 12
    if h >= 0 and h < 12:
        print(f'{h}:{m} A.M')
    elif h >= 12 and h < 24:
        print(f'{hora_nova}:{m} P.M')


def saida():
    hora = 100
    while hora != 99:
        hora = int(input('Informe a hora: '))
        minuto = int(input('Informe os minutos: '))
        conversao(hora, minuto)


# Main Program
saida()