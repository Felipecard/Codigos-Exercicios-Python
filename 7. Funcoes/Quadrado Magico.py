
def quadrado_magico(n1):
    from random import randint
    n2 = n1 + 8
    quad = []
    a = 2
    cont = 0
    while a == 2:
        for k in range(0, 9):
            n = randint(n1, n2)
            while n in quad:
                n = randint(n1, n2)
            quad.append(n)

        valor = quad[0] + quad[1] + quad[2]
        if quad[3] + quad[4] + quad[5] == valor:
            if quad[6] + quad[7] + quad[8] == valor:
                if quad[0] + quad[3] + quad[6] == valor:
                    if quad[1] + quad[4] + quad[7] == valor:
                        if quad[2] + quad[5] + quad[8] == valor:
                            if quad[0] + quad[4] + quad[8] == valor:
                                if quad[6] + quad[4] + quad[2] == valor:
                                    print(f'{quad[0]}  {quad[1]}  {quad[2]}')
                                    print(f'{quad[3]}  {quad[4]}  {quad[5]}')
                                    print(f'{quad[6]}  {quad[7]}  {quad[8]}')
                                    print('-' * 10)
                                    cont += 1
                                    if cont == 9:
                                        break
        quad.clear()



n1 = int(input('O quadrado magico deve comecar em: '))

quadrado_magico(n1)