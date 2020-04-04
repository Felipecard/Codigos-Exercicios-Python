
lista_saltos = []

while True:
    atleta = str(input('Nome do atleta: '))
    for c in range(1, 6):
        salto = float(input(f'Salto {c}: '))
        lista_saltos.append(salto)

    lig = str(input('Deseja continuar? [S/N] '))
    if lig in 'Nn':
        break

print(lista_saltos)
print('-=' * 30)
melhor_salto = max(lista_saltos)
print(f'Melhor salto = {melhor_salto}')
lista_saltos.remove(melhor_salto)
pior_salto = min(lista_saltos)
print(f'Pior salto = {pior_salto}')
lista_saltos.remove(pior_salto)
print(f'Media dos demais saltos = {sum(lista_saltos) / 3}')
print('-=' * 30)
print('Resultado final:')
print(f'{atleta} ==> {sum(lista_saltos) / 3} ')


