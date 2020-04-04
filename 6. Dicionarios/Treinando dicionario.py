aluno = {}
lista_alunos = []


for c in range(0, quant_alunos):
    aluno['codigo'] = int(input('Codigo do aluno:'))
    aluno['altura'] = int(input('Altura do aluno:'))
    aluno['peso'] = int(input('Peso do aluno:'))
    lista_alunos.append(aluno.copy())
for aluno in lista_alunos:
    for k, v, in aluno.items():
        print(f'O campo {k} tem valor {v}')