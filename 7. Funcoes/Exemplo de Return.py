
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')

# O return, nesse caso, ira retornar o valor de S pro r1, r2 e r3
# O (=0) na definicao da funcao, iguala o valor a 0, CASO nao seja atribuido nenhum valor a ele

# o Return ira retornar o resultado da funcao em algo q vc queira... um variavel, uma lista, tupla, numero.....

# -----------------------------------------------------------
def trans(o):
    novo = str(o)
    return novo


n = float(input('Nuemro: '))

print(len(trans(n)))

# O Return deu o valor de 'novo' pra funcao... mas 'novo' nao virou uma variavel externa. Voce tera que chamar a funcao,
# agora sim ela sera o 'nono'