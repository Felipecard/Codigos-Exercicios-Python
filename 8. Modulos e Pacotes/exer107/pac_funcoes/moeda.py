def aumentar(v=0, p1=0, form=False):
    porc = (v * p1) / 100
    res = porc + v
    if form is False:
        return res
    else:
        return formata(res)


def diminuir(v=0, p2=0, form=False):
    porc = (v * p2) / 100
    res = v - porc
    if form is False:
        return res
    else:
        return formata(res)


def metade(v=0, form=False):
    res = v / 2
    return res if not form else formata(res)


def dobro(v=0, form=False):
    res = v * 2
    return res if not form else formata(res)

def formata(v=0, moeda ='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')


# User Interface
def ui(valor=0, p1=10, p2=5):
    print('-=' * 15)
    print('    RESUMO DO VALOR')
    print('-=' * 15)
    print(f'Preco Analisado: \t{formata(valor)}')
    print(f'Dobro do Preco: \t{dobro(valor, True)}')
    print(f'Metade do preco: \t{metade(valor, True)}')
    print(f'{aumentar(p1)}% de aumento: \t{aumentar(valor, p1, True)}')
    print(f'{diminuir(p2)}% de reducao: \t{diminuir(valor, p2, True)}')
    print('-=' * 15)

