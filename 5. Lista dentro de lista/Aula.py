
galera = []
dado = []
tot_maior = 0
tot_menor = 0

for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Nome: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        tot_maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        tot_menor += 1

print(f'Temos {tot_maior} maiores e {tot_menor} menores de idade')