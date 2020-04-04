from time import sleep

def contador(a, b, pulo):
    print('-=' * 20)
    print(f'Contagem de 1 ate 10 de 1 em 1:')

    while a <= b:
        print(a, end=' ')
        sleep(0.5)
        a = a + pulo
    while a >= b:
        print(a, end=' ')
        sleep(0.5)
        a = a - pulo
    print('FIM!')



contador(1, 10, 1)
contador(10, 0, 2)
a = int(input('Inicio: '))
b = int(input('Fim: '))
pulo = int(input('Passo: '))
contador(a, b, pulo)