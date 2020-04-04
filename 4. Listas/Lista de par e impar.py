
todos = []
pares = []
impares = []

for c in range(1, 11):
    n = int(input('Numero: '))
    todos.append(n)

for v in todos:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(todos)
print(pares)
print(impares)

