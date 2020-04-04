from random import randint


def cabecalho():
    print('\033[34m-=\033[m' * 20)
    print('           \033[33mJOGO DA FORCA\033[m')
    print('\033[34m-=\033[m' * 20)
    print()


def escolhe_palavra():
    lista_palavras = []
    arquivo = open('palavras_secretas.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        lista_palavras.append(linha)
    arquivo.close()

    palavra = lista_palavras[randint(0, 13)]
    palavra = palavra.upper()
    return palavra


def letras(palavra):
    n_letras = len(palavra)
    print(f'A palavra tem {n_letras} letras:')
    print()
    return n_letras


def faz_espacos(n_letras):
    lista_espacos = []
    for k in range(0, n_letras):
        lista_espacos.append(' _ ')
    for k in lista_espacos:
        print(k, end='')
    print()
    print()
    return lista_espacos


def logica(palavra, n_letras, lista_espacos):
    erros = 1
    while erros < 7:
        letra = str(input('Escreva uma letra: '))
        letra.upper()
        o = 0
        if letra in palavra:
            for k in range(0, n_letras):
                if letra == palavra[o]:
                    lista_espacos[o] = letra.upper()
                o += 1
            for k in lista_espacos:
                print(k, end='')
            print()
        else:
            print(f'\033[31mVoce ERROU pela {erros}ª vez! Tente novamente...\033[m')
            erros += 1
            for k in lista_espacos:
                print(k, end='')
            print()
        print('_' * 30)

        if not ' _ ' in lista_espacos:
            print('\033[34mPARABENS, VOCE GANHOU!!!\033[m')
            break
    print('\033[31mGAME OVER :(\033[m')


# RODA JOGO
cabecalho()

palavra = escolhe_palavra()
n_letras = letras(palavra)
lista_espacos = faz_espacos(n_letras)

logica(palavra, n_letras, lista_espacos)
