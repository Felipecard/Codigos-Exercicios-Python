
print("BARRACA DE FRUTAS")

qt_morango = float(input("Quantos Kgs de morango?"))
qt_maca = float(input("Quantos Kgs de macã?"))

if(qt_morango < 5):
    preco_morango = qt_morango * 2.5
elif(qt_morango >= 5):
    preco_morango = qt_morango * 2.2

if(qt_maca < 5):
    preco_maca = qt_maca * 1.8
elif(qt_maca >= 5):
    preco_maca = qt_maca * 1.5

peso_total = qt_maca + qt_morango
preco_total = preco_morango + preco_maca
print("Foi comprado {}KG de frutas, dando um total de: R${}".format(peso_total, preco_total))

if(peso_total > 8 or preco_total > 25):
    desconto = (preco_total * 10) / 100
    preco_desconto = preco_total - desconto
    print("Pela quantidade comprada, o cliente ganhou um desconto de 10%, o novo valor é:", preco_desconto)
else:
    print("Voce nao ganhou descontos e o preco mantem", preco_total)

