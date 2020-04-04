

print("POSTO DE GASOLINA")

comb = input("Qual combustivel?")
litros = float(input("Quantos litros?"))

if(comb == "alcool"):
    print("Combustivel escolhido: ALCOOL")
    if(litros < 20):
        valor_alcool1 = litros * 1.9 - (3 * litros) / 100
        print("O preco de {} litros de alcool, com 3% de desconto, sera de: R$ {}".format(litros, valor_alcool1))
    elif(litros >= 20):
        valor_alcool2 = litros * 1.9 - (5 * litros) / 100
        print("O preco de {} litros de alcool, com 5% de desconto, sera de: R$ {}".format(litros, valor_alcool2))
elif(comb == "gasolina"):
    print("Combustivel escolhido: GASOLINA")
    if(litros < 20):
        valor_gasolina1 = litros * 2.5 - (4 * litros) / 100
        print("O preco de {} litros de gasolina, com 4% de desconto, sera de: R$ {}".format(litros, valor_gasolina1))
    elif(litros >= 20):
        valor_gasolina2 = litros * 2.5 - (6 * litros) / 100
        print("O preco de {} litros de gasolina, com 6% de desconto, sera de: R$ {}".format(litros, valor_gasolina2))
else:
    print("Combustivel INVALIDO, insira o nome corretamente")



