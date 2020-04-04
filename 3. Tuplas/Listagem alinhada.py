
material = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('=' * 35)
print('        LISTAGEM DE PRECOS      ')
print('=' * 35)
mat = 0
preco = 1
while(preco <= 18):
    print(f'{material[mat]:.<30} R$ {material[preco]:>5}')
    mat += 2
    preco += 2
print('=' * 40)
