
aluno = {}
lista_geral = []
quant_alunos = int(input('Quantos alunos tem na academia?'))


for c in range(0, quant_alunos):
    aluno['codigo'] = int(input('Codigo do aluno:'))
    aluno['altura'] = float(input('Altura do aluno:'))
    aluno['peso'] = float(input('Peso do aluno:'))
    lista_geral.append(aluno.copy())
    print('-=' * 30)

lista_peso = []
lista_altura = []
for c in lista_geral:
    lista_peso.append(c['peso'])
    lista_altura.append(c['altura'])

mais_alto = max(lista_altura)
mais_baixo = min(lista_altura)
mais_pesado = max(lista_peso)
mais_magro = min(lista_peso)

for c in lista_geral:
    if c['peso'] == mais_pesado:
        print(f'O codigo do aluno mais PESADO é {c["codigo"]} e ele tem {mais_pesado}Kg')
    if c['peso'] == mais_magro:
        print(f'O codigo do aluno mais MAGRO é {c["codigo"]} e ele tem {mais_magro}Kg')
    if c['altura'] == mais_alto:
        print(f'O codigo do aluno mais ALTO é {c["codigo"]} e ele tem {mais_alto}m')
    if c['altura'] == mais_baixo:
        print(f'O codigo do aluno mais BAIXO é {c["codigo"]} e ele tem {mais_baixo}m')
print('--' * 30)

soma_altura = 0
soma_peso = 0
for c in lista_geral:
    soma_altura += c['altura']
    soma_peso += c['peso']

print(f'A media de ALTURA dos alunos é de {soma_altura / quant_alunos}')
print(f'A media de PESO dos alunos é de {soma_peso / quant_alunos}')
print('--' * 30)