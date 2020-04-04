
def fatorial(num, show=0):
    f = 1
    while num > 0:
        if show:
            print(f'{num}', end='')
            if num > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= num
        num -= 1
    return f

# Main Program
numero = int(input('Digite um numero... '))
print(fatorial(numero, show=True))