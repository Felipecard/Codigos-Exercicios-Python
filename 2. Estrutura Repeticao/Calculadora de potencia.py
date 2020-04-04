
print("Calculadora de Potencia")

x = int(input("Diga um numero..."))
y = int(input("Diga outro numero que sera elevado ao anterior..."))

elev = 2
result = x

while(elev <= y):
    result = x * result
    elev = elev + 1
print(result)
