
numeros = 0
rodada = False

while (not rodada):

	rodada = numeros == 4


	numeros = numeros + 1

	print(numeros - 1)



input("Fim")


# enquanto o while nao for falso, repetir: ou podemos dizer tambem, se o while for True, para o laco imediatamente:

# rodada = 0 eh igual a 4? False
# rodada = 1 eh igual a 4? False
# rodada = 2 eh igual a 4? False
# rodada = 3 eh igual a 4? False
# rodada = 4 eh igual a 4? TRUE (FECHA O LACO AQUI) pq agora... rodada = True
