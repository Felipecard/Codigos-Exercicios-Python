print('Consulta tabela brasileirao 2019')

tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Atl Paranaense', 'Sao Paulo', 'Inter', 'Corinthias',
           'Fortaleza', 'Goias', 'Bahia', 'Vasco', 'Atletico MG', 'Fluminense', 'Botafogo',
           'Ceara', 'Cruzeiro', 'CSA', 'Chape', 'Avai')


print(f'A) Irão para libertadores: {tabela[0:5]}')
print(f'B) Serao rebaixados: {tabela[15:19]}')
print('-=' * 30)
print(f'C) Lista dos times em ordem alfabetica: {sorted(tabela)}')
time = str(input('De qual time voce gostaria de saber a colocacao final? '))
posicao = tabela.index(time)
print(f'D) O time {time} ficou na posicao {posicao + 1}')
