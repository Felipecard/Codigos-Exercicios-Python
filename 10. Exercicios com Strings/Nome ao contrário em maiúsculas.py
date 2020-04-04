
def pedenome():
    nome = str(input('Nome: '))
    return nome


def nomecontrario(n):
    return n.upper()


def embaralha(n):
    from random import randint
    s = sorted(n)
    tam = len(s)
    s[0] = s[randint(0, tam)]

    cont = 0
    for c in range(0, tam):
        print(s[cont], end='')
        cont += 1



p = pedenome()
c = nomecontrario(p)
e = embaralha(c)

e
