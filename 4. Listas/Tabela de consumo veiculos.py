
lista_marca = []
lista_capacidade = []

for k in range(1, 6):
    marca = str(input(f'Marca do carro {k}: '))
    capacidade = float(input(f'Quantos Km o {marca} faz por litro de gasolina: '))
    lista_marca.append(marca)
    lista_capacidade.append(capacidade)
print(lista_marca)
print(lista_capacidade)

print('RELATORIO FINAL')
print('N    Marca        Km por litro           Litros em 1000 Km          Custo')
o = 0
maior = 0
for k in range(1, 6):
    litros_gastos = 1000 / lista_capacidade[o]
    print(f'{k} - {lista_marca[o]}      -  {lista_capacidade[o]}        -       {litros_gastos:.2f} Litros        -        R$ {litros_gastos * 2.25:.2f} ')
    if lista_capacidade[o] > maior:
        maior = lista_capacidade[o]
    o += 1
print('-=' * 30)
p = 0
for k in range(1, 6):
    if maior == lista_capacidade[p]:
        print(f'O menor consumo é do {lista_marca[p]}')
    p += 1
