
def lanca_dados():
    from random import randint
    l1 = randint(1, 6)
    l2 = randint(1, 6)
    lance = l1 + l2
    return lance


cont = 1
jogo = lanca_dados()
while jogo < 12:
    if jogo == 7 or jogo == 11:
        print(f'O jogador {cont} é um NATURAL, tirou {jogo} e GANHOU O JOGO!')
        break
    elif jogo == 2 or jogo == 3 or jogo == 12:
        print(f'O jogador {cont} é um CRAPS, tirou {jogo} e PERDEU o jogo!')
        break
    else:
        print(f' Jogador {cont}, este é seu ponto: {jogo}, continue jogando....')
        jogo2 = 5
        while jogo2 < 12:
            jogo2 = lanca_dados()
            if jogo2 == jogo:
                print(f'Seu novo numero é {jogo2}, mesmo do anterior: {jogo}. PARABENS, voce GANHOU!')
                break
            elif jogo2 == 7:
                print(f'Seu novo numero é: {jogo2}, igual a 7. VOCE PERDEU!')
                break
            print(f'Nao tirou {jogo} e nem 7. Jogue novamente....')
        break

