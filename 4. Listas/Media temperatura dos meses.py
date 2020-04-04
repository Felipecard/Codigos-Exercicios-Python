meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media_mes = []
cont_mes = 1
for c in range(1, 13):
    media_mes.append(int(input(f'Media do mes {cont_mes} ')))
    cont_mes += 1

media_todos = sum(media_mes) / 12
print(media_todos)
v = 0
print('-' * 30)
print('Os meses de:')
for c in range(1, 13):
    if media_mes[v] > media_todos:
        print(f'{meses[v]}, com {media_mes[v]}oC,')
    v += 1
print('tiveram a temperatura acima da media anual')
