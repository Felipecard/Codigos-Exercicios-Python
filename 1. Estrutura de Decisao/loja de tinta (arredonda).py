
print("Programa para loja de tintas")

metros = float(input("Quantos metros quadrados voce precisa pintar?"))

quant_litros = metros / 3
print("Voce precisara de {} litros de tinta".format(quant_litros))

quant_latas = quant_litros / 18
print("Voce precisara de {} latas".format(quant_latas))

quant_latas = int(quant_latas)

if(quant_latas % 100 == 0):
    print(quant_latas)
else:
    print(quant_latas + 1)

preco = quant_latas * 80
print("Voce devera pagar R$ {} por {} latas".format(preco, quant_latas))