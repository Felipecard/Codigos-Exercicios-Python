
print("Mostre a quantidade de 5 números:  a quantidade de números ímpares e pares.")

n = 1
P = 0
I = 0
while(n <= 5):
    a = int(input("Coloque um numero.."))
    n = n + 1
    if(a % 2 == 0):
        a = P
        P = P + 1
    else:
        a = I
        I = I + 1

print("A qtd de números pares é: ", P)
print("A qtd de números ímpares é: ", I)

