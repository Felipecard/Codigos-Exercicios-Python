
print("LADOS DO TRIANGULO")

lado1 = float(input("Diga o lado 1"))
lado2 = float(input("Diga o lado 2"))
lado3 = float(input("Diga o lado 3"))


if((lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado3 + lado2) > lado1):
    print("É um triangulo:")
    if(lado1 == lado2 == lado3):
        print(" Equilatero")
    elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print("Isósceles")
    elif(lado1 != lado2 != lado3):
        print("Escaleno")
else:
    print("Nao é um triangulo")


