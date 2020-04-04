lista_sal = []
sal = 55
cont = 0

while sal != 0:
    sal = float(input('Salario: '))
    if sal != 0:
        lista_sal.append(sal)
        cont += 1
print(lista_sal)
o = 0
valor_min = 0
total_abonos = 0
maior = 0
print('PROJECAO DE GASTOS COM ABONOS:')
print('Salario             Abono')
print('-' * 30)
for k in range(0, cont):
    if lista_sal[o] > 500:
        abono = (20 * lista_sal[o]) / 100
        if abono > maior:
            maior = abono
        print(f'R$ {lista_sal[o]}       R$ {abono}')
    else:
        abono = 100
        valor_min += 1
        print(f'R$ {lista_sal[o]}        R$ {abono}')
    total_abonos += abono
    o += 1

print('-=' * 30)
print(f'Foram processados {cont} colaboradores')
print(f'Total gasto com abonos: R$ {total_abonos}')
print(f'Valor minino pago a {valor_min} colaboradores')
print(f'O maior valor de abono pago foi : R$ {maior}')