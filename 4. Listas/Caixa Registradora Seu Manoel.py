print("CAIXA REGISTRADORA DO SEU MANOEL")

ligada = 1
while(ligada == 1):

    cont = 1
    qt_produtos = 0
    lista_produtos = []

    while(cont != qt_produtos):
        preco_produto = float(input("Registre o preco do produto..."))
        if(preco_produto != 0):
            lista_produtos.append(preco_produto)
            qt_produtos += 1
            cont += 1
        elif(preco_produto == 0):
            cont = qt_produtos

    nome = 1
    somatorio_precos_produtos = 0
    print("~" * 30)
    print("LOJAS TABAJARA")
    print("~" * 30)
    for preco_produto in lista_produtos:
        print("Produto R$ {} = R$ {}".format(nome, preco_produto))
        nome += 1
        somatorio_precos_produtos += preco_produto

    print("TOTAL: R$", somatorio_precos_produtos)
    print("~" * 30)
    dinheiro = int(input("Dinheiro: R$"))
    print("Troco: R$", dinheiro - somatorio_precos_produtos)
    print("~" * 30)