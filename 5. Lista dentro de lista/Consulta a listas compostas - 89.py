print('Consulta a listas compostas - 89')

ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    liga = str(input('Quer continuar? [S/N]'))
    if(liga in 'Nn'):
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 25)
for cont, valor in enumerate(ficha):
    print(f'{cont:<4}{valor[0]:<10}{valor[2]:>8}')
print('-=' * 30)
while True:
    gov = int(input('Mostrar notas de qual aluno: (999 interrompe) '))
    if(gov == 999):
        print('Finalizando...')
        break
    elif(gov <= cont):
        print(f'Notas de {ficha[gov][0]} sao {ficha[gov][1]}')

print('<<< VOLTE SEMPRE >>>')


