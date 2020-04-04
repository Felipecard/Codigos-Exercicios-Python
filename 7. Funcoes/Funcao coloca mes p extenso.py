
def data(d, m, a):
    lista_mes = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho','Julho', 'Agosto','Stembro', 'Outubro', 'Novembro', 'Dezembro']
    if d < 0 or d > 31 or m < 0 or m > 12 or a < 0 or a > 2020:
        print('Data Invalida')
    else:
        print(f'{d}/{lista_mes[m - 1]}/{a}')



d = int(input('Dia: '))
m = int(input('Mes: '))
a = int(input('Ano: '))

data(d, m, a)