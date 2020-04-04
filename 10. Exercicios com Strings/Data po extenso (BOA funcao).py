
def pededata():
    print('Data de Nascimento:')
    d = int(input('Dia: '))
    m = int(input('Mes: '))
    a = int(input('Ano: '))
    return d, m, a


def mesextenso(m):
    lista_meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho',
                   'Julho', 'Agosto', 'Stembro', 'Outrubro', 'Novembro', 'Dezembro']
    return lista_meses[m - 1]


z = pededata()
print(f' DATA:  {z[0]} / {mesextenso(z[1])} / {z[2]}')