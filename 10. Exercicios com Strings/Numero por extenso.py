desliga = 0
n = str(input('Numero ate 99: '))
len = len(n)
lista_unidades = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
lista_dezenas = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezoito', 'dezenove']
lista_redondos = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

if len == 1:
    n = int(n)
    o = 0
    for k in range(1, 9):
        if o + 1 == n:
            print(lista_unidades[o])
        o += 1
        desliga = 5

elif len == 2:
    n = int(n)
    o = 0
    for k in range(1, 9):
        if o + 10 == n:
            print(lista_dezenas[o])
            desliga = 5
        o += 1


num = []
y = int(n)

if y > 19:
    y = str(n)
    for k in y:
        num.append(k)

y = int(n)
j = 0
p = 20

if desliga == 0:
    if num[1] == '0':
        for v in range(1, 8):
            if p == n:
                red = lista_redondos[j]
                print(lista_redondos[j])
            j += 1
            p += 10

    k = 2
    if num[1] != '0':
        for v in range(1, 8):
            if str(k) == num[0]:
                red = lista_redondos[j]
            j += 1
            p += 10
            k += 1
        i = 0
        for v in range(1, 9):
            if str(i + 1) == num[1]:
                print(f'{red} e {lista_unidades[i]}')
            i += 1
