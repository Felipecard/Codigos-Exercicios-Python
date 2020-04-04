
print("Maior e menor valor de um conjunto de numeros, o conjunto nao aceitará numeros maiores que 1000")

cont = 1
n = []


while(cont <= 5):
    numero = int(input("Escreva 5 numeors.."))
    if(numero > 1000 or numero < 0):
        numero = 0
    else:
        n.append(numero)
    cont += 1

print("Os numeros escolhidos, foram: ", n)

max = max(n)
min = min(n)

print("O maior numero é:", max)
print("O menor numero é:", min)

soma_dos_numeros = 0
for numeros in n:
    soma_dos_numeros = soma_dos_numeros + numeros
print("A Soma dos numeros é: ", soma_dos_numeros)