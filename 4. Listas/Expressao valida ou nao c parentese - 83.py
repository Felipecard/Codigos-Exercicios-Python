
print('Exercicio 83')

expressao = []
expressao.append(str(input('Coloque a expressao: ')))


for c in expressao[0]:
    parentese_esq = expressao[0].count('(')
    parentese_dir = expressao[0].count(')')

if(parentese_esq == parentese_dir):
    print('Expressao Valida')
else:
    print('Expressao Invalida')
