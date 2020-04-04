print('           << MENU >>            ')
print('Especificação   Código  Preço')
print('Cachorro Quente 100     R$ 5,00')
print('Bauru Simples   101     R$ 7,30')
print('X - Tudão       102     R$ 8,50')
print('Hambúrguer      103     R$ 5,20')
print('X - burguer     104     R$ 6,30')
print('Refrigerante    105     R$ 4,00')
print('-=' * 30)

lista_geral = []
lanche = {}

while True:
    lanche['pedido'] = int(input('Qual seu pedido? Insira o codigo do produto...  '))
    lanche['quant'] = int(input(f'Qual a quantidade? '))
    lista_geral.append(lanche.copy())

    ligado = str(input('Deseja continuar o pedido? [S/N] '))
    if ligado in 'Nn':
        break

ped1 = ped2 = ped3 = ped4 = ped5 = ped6 = 0
print('PEDIDO: ')
for l in lista_geral:
    if l['pedido'] == 100:
        l['pedido'] = 5.0
        ped1 = l['pedido'] * l['quant']
        print(f'Cachorro quente x {l["quant"]}....... R${ped1}')
    if l['pedido'] == 101:
        l['pedido'] = 7.30
        ped2 = l['pedido'] * l['quant']
        print(f'Bauru Simples x {l["quant"]}....... R$ {ped2}')
    if l['pedido'] == 102:
        l['pedido'] = 8.50
        ped3 = l['pedido'] * l['quant']
        print(f'X - Tudão x {l["quant"]}........... R$ {ped3}')
    if l['pedido'] == 103:
        l['pedido'] = 5.20
        ped4 = l['pedido'] * l['quant']
        print(f'Hamburguer x {l["quant"]}.......... R$ {ped4}')
    if l['pedido'] == 104:
        l['pedido'] = 6.30
        ped5 = l['pedido'] * l['quant']
        print(f'X - burguer x {l["quant"]}......... R$ {ped5}')
    if l['pedido'] == 105:
        l['pedido'] = 4.00
        ped6 = l['pedido'] * l['quant']
        print(f'Refrigerante x {l["quant"]}........ R$ {ped6}')
print('-' * 30)
print(f'TOTAL: {ped1 + ped2 + ped3 + ped4 + ped5 + ped6:.2f}')
print('-' * 30)
print()
print('Volte Sempre :)')




