from random import randint

print('Cinco numeros')

numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

min = min(numeros)
max = max(numeros)

print(numeros)
print(min)
print(max)