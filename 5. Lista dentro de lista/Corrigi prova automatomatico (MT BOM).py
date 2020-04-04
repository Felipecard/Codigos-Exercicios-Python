
gabarito = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a']
lista_geral = []
cada_prova = []
n = 1
quant_alunos = 0
while True:
    for n in range(1, 11):
        cada_prova.append(str(input(f'Questão {n}')))

    lista_geral.append(cada_prova[:])
    cada_prova.clear()
    ligado = str(input('Deseja continuar? '))
    quant_alunos += 1
    if ligado in 'Nn':
            break


print(f'A quantidade de alunos é {quant_alunos}')
lista_result = []
a = 0
for j in range(0, quant_alunos):
    nota_aluno = 0
    v = 0
    for c in range(1, 11):
        if lista_geral[a][v] == gabarito[v]:
            nota_aluno += 1
        v += 1
    lista_result.append(nota_aluno)
    a += 1

print(f'O maior nota foi {max(lista_result)}')
print(f'A menor nota foi {min(lista_result)}')
print(f'A media de notas da turma é {sum(lista_result) / quant_alunos}')




