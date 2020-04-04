
print("NOTA ENTRE 0 E 10")

valor = int(input("Informe um valor de 0 a 10"))

while(valor > 10 or valor < 0):
    print("Valor invalido")
    valor = int(input("Apresente outro numero:"))

print("valor: {} aceito".format(valor))


