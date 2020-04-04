from random import randint
from time import sleep

def sorteia(lista):
    for c in range(0, 5):
        n = randint(1, 20)
        lista.append(n)
        print(n, end=' ')
        sleep(0.3)
    print('FIM!')

def somapar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos {soma}')

# Main Program
numeros = []
sorteia(numeros)
somapar(numeros)

