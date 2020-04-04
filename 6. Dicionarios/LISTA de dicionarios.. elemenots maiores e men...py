cidade = {}
listageral = []
soma = 1
total_carros = 0
for c in range(1, 6):
    cidade['cod_cidade'] = str(input('Codigo da Cidade: '))
    cidade['n_carro'] = int(input('Numero de Veicilos: '))
    cidade['n_acidente'] = int(input('Numero de Acidentes com vítima: '))
    listageral.append(cidade.copy())
    soma += 1
    print('-=' * 30)

print(listageral)
print('-=' * 30)

lista_acidente = []
for c in listageral:
    lista_acidente.append(c['n_acidente'])
    total_carros += c['n_carro']
maior_n_acidente = max(lista_acidente)
menor_n_acidente = min(lista_acidente)

for c in listageral:
    if c['n_acidente'] == maior_n_acidente:
        print(f'O maior indice de acidentes é em {c["cod_cidade"]} com {maior_n_acidente} acidentes')
    if c['n_acidente'] == menor_n_acidente:
        print(f'O menor indice de acidentes é em {c["cod_cidade"]} com {menor_n_acidente} acidentes')
print('-=' * 30)
print(f'A media de veiculos em todas as cidades é {total_carros / soma}')
n = 0
soma_cidades_peq = 0
for c in listageral:
    if c['n_carro'] < 2000:
        soma_cidades_peq += c['n_acidente']
        n += 1
print(f'A média de acidentes nas cidades com menos de 2.000 veículos é {soma_cidades_peq / n}')