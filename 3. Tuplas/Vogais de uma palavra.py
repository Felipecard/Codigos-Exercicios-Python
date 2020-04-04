
palavras = ('dedo', 'costas', 'olho', 'perna', 'orelha')

pal = 0
while(pal <= len(palavras)):
    print(f'A palavra {palavras[pal]} tem as vogais:')
    for letra in sorted(palavras[pal]):
        if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
            print(f' {letra} ')
    print('-' * 30)
    pal += 1

# for palavra in palavras:
    #print('Na palabra {palavra} temos:)
    #for letra in palavra:
        #if...