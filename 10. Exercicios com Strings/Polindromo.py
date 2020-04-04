

def pedefrase():
    frase = str(input('Frase: '))
    return frase


def polindromo(frase):
    frase2 = frase.replace(' ', '')
    if frase2 == frase2[::-1]:
        print('É um Polindromo')
    else:
        print('Nao é um Polindromo')


# MAIN PROGRAM
polindromo(pedefrase())









