
numeros = []
impar = []
par = []

for cont in range(0, 7):
    n = (int(input(f'Digite o {cont + 1}o valor: ')))
    if(n % 2 == 0):
        par.append(n)
    else:
        impar.append(n)

numeros.append(par)
numeros.append(impar)

print(f'Valores pares em ordem crescente: {sorted(par)}')
print(f'Valores impares em ordem crescente: {sorted(impar)}')

