
from random import randint
lista = []
dici = {}

for cont in range(1, 11):
    dici[cont] = randint(50, 100)
print(dici)

maior_peso = 50
for k, v in dici.items():
    if v > maior_peso:
        maior_peso = v

for k, v in dici.items():
    if v == maior_peso:
        print(f'O aluno {k}, tem o maior peso: {maior_peso}kg')

menor_peso = 100
for k, v in dici.items():
    if v < menor_peso:
        menor_peso = v

for k, v in dici.items():
    if v == menor_peso:
        print(f'O aluno {k}, tem o menor peso: {menor_peso}kg')


