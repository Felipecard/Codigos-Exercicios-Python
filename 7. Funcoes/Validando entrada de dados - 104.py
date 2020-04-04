
def leiaint(txt):
    ok = False
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        if ok == True:   #Poderia tambem se -- if ok: --
            break
    return valor

n = leiaint('Digite um nuemro inteiro:  ')
print(f'O numero que acabou de digitar é {n}')

