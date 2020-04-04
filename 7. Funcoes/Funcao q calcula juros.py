
def valor_pagamento(v, d):
    if d == 0:
        return v
    elif d > 0:
        taxa = 3 + (0.1 * d)
        multa = (v * taxa) / 100
        valor_prest_final = v + multa
        return valor_prest_final


# MAIN
cont = 0
lista_dia = []
valor_prest = 10
while valor_prest != 0:
    valor_prest = float(input('Valor da prestacao: '))
    dias_atraso = int(input('Dias de atraso '))
    print(valor_pagamento(valor_prest, dias_atraso))
    if valor_prest != 0:
        lista_dia.append(valor_pagamento(valor_prest, dias_atraso))
        cont += 1

print('RALATORIO DO DIA')
print('-' * 40)
print(f'Foram feitas {cont} consultas')
o = 0
for k in range(0, cont):
    print(f'Consulta {k + 1}....... R$ {lista_dia[o]}')
    o += 1
print(f'O valor total de prestacoes no dia foi: {sum(lista_dia)}')