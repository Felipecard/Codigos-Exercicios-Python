print('Tuplas')

a= (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))



# Varias maneiras de fazer a mesma coisa

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}')

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {posicao}')