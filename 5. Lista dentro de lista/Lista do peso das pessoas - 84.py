
print('Lista do peso das pessoas - 84')

galera = []
pessoa = []
max = min = 0 #ou max = 0 - min = 0


while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if(len(galera) == 0):
        max = min = pessoa[1]
    else:
        if(pessoa[1] > max):
            max = pessoa[1]
        if(pessoa[1] < min):
            min = pessoa[1]
    galera.append(pessoa[:])
    pessoa.clear()

    resp = str(input('Quer continuar? [S/N} '))
    if resp in 'Nn':
        break

print(galera)
print(f'Ao todo voce cadastrou {len(galera)} pessoas')
peso = []

print(f'O maior peso foi de {max}Kg. Peso de ', end='')
for p in galera:
    if(p[1] == max):
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {min}Kg. Peso de ', end='')
for p in galera:
    if(p[1] == min):
        print(f'{p[0]} ', end='')
print()
