
print('Consultando valores na Tupla')
#Para pedia colocar os numeros em uma tupla. Ele fez o imput ja dentro da tipla - valores = (input('Digite um n'))

valores = []
cont = 1
while(cont <= 4):
    v = int(input('Digite um valor'))
    valores.append(v)
    cont +=1

print(valores)
valor_nove = 0

for v in valores:
    if (v == 9):
        valor_nove += 1
print(f'O valor NOVE, aparece {valor_nove} vez(es)')


if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)} posicao')
else:
    print('O valor 3 nao foi digitado')


print(f'Os valores pares sao: ')
for v in valores:
    if(v % 2 == 0):
        print(f'{v}  ', end='')

