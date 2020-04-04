
print("FATORIAL")

continua = "s"
while(continua == "s"):
    n = int(input("Coloque um numero inteiro, positivo e menor que 16: "))
    c = n
    f = 1
    if(n > 0 and n < 16):
        while(c > 1):
            f = f * c  #para calcular fatorial
            c -= 1
        print(f)
    else:
        print("Numero invalido")

        continua = (input("Quer saber outro fatorial? (s) ou (n)"))

