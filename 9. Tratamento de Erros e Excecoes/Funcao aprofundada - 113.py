
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interropinda pelo usuario')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interropinda pelo usuario')
            return 0
        else:
            return n


n1 = leiaint('Digite um nuemro inteiro:  ')
print(f'O numero {n1}, que acabou de digitar é valido ')
print()
n2 = leiafloat('Digite um nuemro real:  ')
print(f'O numero {n2}, que acabou de digitar é realmente real ')