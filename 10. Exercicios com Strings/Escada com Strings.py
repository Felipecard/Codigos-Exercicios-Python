
def pedenome():
    nome = str(input('NOME: '))
    return nome.upper()


def escada(n):
    letras = len(n)
    o = 0
    l = 1
    while o < letras:
        o = 0
        for c in range(0, l):
            print(n[o], end='')
            o += 1
        l += 1
        print()


# Main
vert = escada(pedenome())
