
todos = []
cada_aluno = []
qunt_alunos = 5
for a in range(1, qunt_alunos):
    print(f'<< Notas do Aluno {a} >>')
    for c in range(1, 5):
        nota = float(input(f'Nota {c}: '))
        cada_aluno.append(nota)
    todos.append(cada_aluno[:])
    cada_aluno.clear()
print(todos)
print('-=' * 30)
media = []

for s in todos:
    soma = sum(s)
    med = soma / 4
    media.append(med)
print(f'As medias foram: {media}')
bons = 0
for b in media:
    if b >= 7:
        bons += 1
print(f'Tiveram {bons} alunos com media maior que 7')