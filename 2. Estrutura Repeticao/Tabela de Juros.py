

divida = float(input('Valor da divida: '))
qt_parcelas = 3
juros = 10

print(f'{"Qt de parcelas"} | {"Juros":>5} | {"Valor da divida":>15} | {"Valor da parcela":>15}')
print(f'{1}{0:>17}%      R${divida:>5}          R${divida / 1:>5.2f}')
valor_acrec2 = (divida * 10) / 100
divida2 = divida + valor_acrec2
print(f'{3}{10:>17}%      R${divida2:>5}          R${divida2 / 3:>5.2f}')

for c in range(1, 3):
    qt_parcelas += 3
    juros += 5
    valor_acrec = (divida2 * juros) / 100
    divida2 = divida2 + valor_acrec
    print(f'{qt_parcelas}{juros:>17}%      R${divida2:>5}          R${divida2 / qt_parcelas:>5.2f}')