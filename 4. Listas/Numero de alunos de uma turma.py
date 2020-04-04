
quant_turma = int(input("Quantas turmas tem na escola?"))
lista_turmas = []
cont = 1
numero_turma = 1

while(cont <= quant_turma):
    turma = int(input("Quantidade de aluno na turma {}?".format(numero_turma)))
    if(turma <= 40):
        lista_turmas.append(turma)
        cont += 1
        numero_turma += 1
    else:
        print("Uma turma nao pode ter mais de 40 alunos")
print(lista_turmas)

total_alunos_escola = 0
for turma in lista_turmas:
    total_alunos_escola += turma
print(total_alunos_escola)

media_turmas = total_alunos_escola / quant_turma
print(media_turmas)