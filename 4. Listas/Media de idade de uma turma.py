
cont = 1
z = 1
n = int(input("Quantas pessoas existem na turma?"))
lista_idades = []

while(cont <= n):
    idade_aluno = int(input("Idade do aluno {}:".format(z)))
    lista_idades.append(idade_aluno)
    z += 1
    cont += 1
print(lista_idades)

soma_idades = 0
for idade_aluno in lista_idades:
    soma_idades = soma_idades + idade_aluno
media_idade = soma_idades / n
print("A media de idade da turma é de:", media_idade)

if(media_idade > 0 and media_idade <= 25):
    print("É uma turma jovem!")
elif(media_idade >= 26 and media_idade < 60):
    print("É uma turma adulta!")
else:
    print("É uma turma idosa!")
