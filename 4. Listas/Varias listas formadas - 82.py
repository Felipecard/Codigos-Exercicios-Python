print('ex 82 ')

lista = []
pares = []
impares = []
cont = 's'

while(cont == 's'):
    num = int(input('Digite um numero: '))
    lista.append(num)
    if(num % 2 == 0):
        pares.append(num)
    else:
        impares.append(num)
    cont = str(input('Quer continuar? [S/N] '))

print(f'Lista inteira: {lista}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')

