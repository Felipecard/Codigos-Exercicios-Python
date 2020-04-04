from datetime import datetime

print('92 - Cadastro')
cadastro = {}

cadastro['nome'] = str(input('Nome:'))
nascimento = int(input('Ano de Nascimento:'))
cadastro['idade'] = datetime.now().year - nascimento
cadastro['ctps'] = int(input('Nuemro da carteira de trabalho (0 nao tem):'))
if(cadastro['ctps'] != 0):
    cadastro['contrat'] = int(input('Ano de Contratacao:'))
    cadastro['salario'] = float(input('Salario: R$'))
    cadastro['aposentadoria'] = ((cadastro['idade'] + cadastro['contrat'] + 35) - datetime.now().year)

print('-= * 30')
for k, v in cadastro.items():
    print(f' -- {k} tem o valor {v}')





