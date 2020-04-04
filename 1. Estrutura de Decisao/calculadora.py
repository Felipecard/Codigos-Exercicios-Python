
print("CALCULADORA BASICA")

continuar = "s"

while (continuar == "s"):

    x = float(input("Insira o primeiro numero..."))
    operacao = input("Qual operacao quer fazer? (+) (-) (*) (/) ou (%)")
    y = float(input("Insira o segundo numero..."))
    print("-------------------------------------")

    if (operacao == "+"):
        z = x + y
        print("{} + {} = {}".format(x, y, z))
    elif (operacao == "-"):
        z = x - y
        print("{} - {} = {}".format(x, y, z))
    elif (operacao == "*"):
        z = x * y
        print("{} * {} = {}".format(x, y, z))
    elif (operacao == "/"):
        z = x / y
        print("{} / {} = {}".format(x, y, z))
    elif (operacao == "%"):
        z = (x * y) / 100
        print("{}% de {} = {}".format(x, y, z))

    print("Fim da operacao")
    print("---------------")



