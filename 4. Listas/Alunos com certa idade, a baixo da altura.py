print()
print('Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine')
print('quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.')
print()
print('-=' * 30)
perfil = [1.70, 14, 1.60, 12, 1.65, 11, 1.80, 15, 1.58, 14, 1.62, 12, 1.53, 11, 1.72, 14, 1.50, 8, 1.60, 14]
alturas = []
v = 1
for c in range(1, 11):
    if perfil[v] > 13:
        alturas.append(perfil[v - 1])
    v += 2
print(alturas)
soma = 0
g = 0
for c in range(1, 11):
    soma += perfil[g]
    g += 2
media = soma / 10

alunos_menor = 0
for c in alturas:
    if c < media:
        alunos_menor += 1
print(f'O total de {alunos_menor} com mais de 13 anos, estao com alturas inferiores a media')