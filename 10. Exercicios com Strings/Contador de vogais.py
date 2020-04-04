
def pedefrase():
    frase = str(input('Frase: '))
    return frase


def espacos(f):
    esp = 0
    for k in f:
        if k == ' ':
            esp += 1
    return esp


def vogais(f):
    a = e = i = o = u = 0
    for k in f:
        if k == 'a':
            a += 1
        if k == 'e':
            e += 1
        if k == 'i':
            i += 1
        if k == 'o':
            o += 1
        if k == 'u':
            u += 1
    return a, e, i, o, u


frase = pedefrase()
esp = espacos(frase)
print(f'Existem {esp} espacos em branco na frase')

vog = vogais(frase)
print(f'A vogal (A) aparece {vog[0]} vezes')
print(f'A vogal (E) aparece {vog[1]} vezes')
print(f'A vogal (I) aparece {vog[2]} vezes')
print(f'A vogal (O) aparece {vog[3]} vezes')
print(f'A vogal (U) aparece {vog[4]} vezes')