
num = []
cont = 's'

while(cont == 's'):
    valor = int(input('Digite um valor...'))
    if valor in num:
        print('Valor duplcado, ele NAO doi adicionado')
    else:
        num.append(valor)
    cont = str(input('Deseja continuar?? [S/N]'))

print(sorted(num))
