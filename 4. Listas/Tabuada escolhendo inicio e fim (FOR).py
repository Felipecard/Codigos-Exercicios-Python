
tabuada = int(input("Tabuada de que numero?"))
inicio = int(input("Comecando em?"))
fim = int(input("E terminando em?"))

if(inicio < fim):
    for cont in range(inicio, fim + 1):
        resultado = cont * tabuada
        print("{} x {} = {}".format(tabuada, inicio, resultado))
        inicio += 1
else:
    print("O numero inicial deve ser menor que o final")

