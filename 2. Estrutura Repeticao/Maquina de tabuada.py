
print("MAQUINA DE TABUADA")

n = int(input("De qual numero deseja saber a tabuada?"))
multiplicador = 1
print("Tabuada de:", n)

while(multiplicador <= 10):
    result = n * multiplicador
    print("{} * {} = {}".format(n, multiplicador, result))
    multiplicador = multiplicador + 1

