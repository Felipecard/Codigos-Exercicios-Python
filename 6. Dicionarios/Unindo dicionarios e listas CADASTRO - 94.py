
print('94 - Unindo dicionarios e listas')

lista_dados = []
pessoa = {}
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [H/M] '))
    pessoa['idade'] = int(input('Idade: '))
    lista_dados.append(pessoa.copy())

    ligado = str(input('Quer continuar? [S/N]'))
    if ligado in 'Nn':
        break
print(lista_dados)
print('-=' * 30)
print(f' ==> O grupo tem {len(lista_dados)} pessoas')

soma = 0
for v in lista_dados:
    soma = soma + v['idade']
media = soma / len(lista_dados)
print(f' ==> A media de idade é {media}')

print(' ==> As mulheres cadastradas foram:', end=' ')
for v in lista_dados:
    if(v['sexo'] in 'Mm'):
        print(v['nome'], end=' ')
print()
print(' ==> Lista das pessoas que estao acima da media:')
for v in lista_dados:
    if(v['idade'] > media):
        print(f'{v["nome"]} - com {v["idade"]} anos')

