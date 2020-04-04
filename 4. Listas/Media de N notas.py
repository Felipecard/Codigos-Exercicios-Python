

print("Media de N notas")

cont = 1
conjunto_notas = []

while(cont <= 5):
    nota = float(input("Diga sua nota..."))
    conjunto_notas.append(nota)
    cont += 1
print(conjunto_notas)

soma_das_notas = 0
for nota in conjunto_notas:
    soma_das_notas = soma_das_notas + nota
print("A media do aluno, foi:", soma_das_notas / 5)