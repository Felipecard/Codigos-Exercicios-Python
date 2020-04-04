
lista = []
cont = 's'

while(cont == 's'):
    num = int(input('Digite um numero: '))
    lista.append(num)
    cont = str(input('Deseja continuar? [S/N] '))
print(lista)

print('-=' * 30)
print(f'A) Foram digitados {len(lista)} numeros')
lista_reversa = sorted(lista, reverse=True)
print(f'B) A lista ordenada de forma decrescente: {lista_reversa}')

if 5 in lista:
    print('C) O valor 5 esta na lista ')
else:
    print('C) O valor 5 nao esta na lista')