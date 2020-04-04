
def embaralha(p):
    from random import randint
    nova_palavra = sorted(p)
    print(nova_palavra)
    tamanho = len(nova_palavra)
    o = randint(0, tamanho - 1)
    nova_palavra[0] = nova_palavra[o]

    l = 0
    print('Resultado final:')
    for k in range(0, tamanho):
        print(nova_palavra[l].upper(), end='')
        l += 1


# MAIN
palavra = str(input('Palavra: '))
embaralha(palavra)