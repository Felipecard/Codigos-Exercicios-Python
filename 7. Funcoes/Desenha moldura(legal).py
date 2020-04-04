
def desenha_moldura(largura, altura):
    while largura < 1:
            largura = int(input('Largura inviavel, coloque outro valor: '))
    while altura < 1:
            altura = int(input('Altura inviavel, coloque outro valor: '))

    print(f'{"+"}{"-" * largura * 2}{"+"}')

    for k in range(0, altura):
        print(f'{"|"}{" " * largura * 2}{"|"}')

    print(f'{"+"}{"-" * largura * 2}{"+"}')


# MAIN PROGRAM
print('-=' * 20)
print('        DESENHA MOLDURA')
print('-=' * 20)
print()
largura = int(input('Largura: '))
altura = int(input('Altura: '))

desenha_moldura(largura, altura)

b = str(input('Gostou do programa?'))