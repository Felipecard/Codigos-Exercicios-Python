
lista_salario = []
cont = 0
while True:
    vendeu = (int(input('Quanto o vendedor vendeu na semana? ')))
    comissao = (9 * vendeu) / 100
    salario = comissao + 200
    lista_salario.append(salario)
    cont += 1

    ligado = str(input('Deseja continuar? [S/N] '))
    if ligado in 'Nn':
        break
print(lista_salario)
posicao = 0

for c in lista_salario:
    posicao += 1
    min = 100
    max = 199
    if c > 1000:
        print(f'Vendedro {posicao}, recebeu salario maior que 1000')
    for d in range(1, 10):
        min += 100
        max += 100
        if c > min and c < max:
            print(f'Vendedro {posicao}, recebeu salario entre ${min} - ${max}')


