
print('93 - Estatisticas GOLS do jogador n')

dados = {}
lista_gols = []
soma = 0

dados['nome'] = str(input('Nome: '))
n_partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, n_partidas):
    gol = int(input(f'Quantos gols na partida {c}?'))
    lista_gols.append(gol)
    soma += gol
dados['gols'] = lista_gols
dados['total'] = soma
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {n_partidas} partidas.')
for p, g in enumerate(lista_gols):
    print(f'=> Na partida {p}, fez {g} gols.')
print(f'Foi um total de {dados["total"]} gols')




