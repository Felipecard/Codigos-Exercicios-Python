
num = 1
grupo025 = 0
grupo2650 = 0
grupo5175 = 0
grupo76100 = 0

while num >= 0:
    num = int(input('Numero: '))
    if num >= 0 and num <= 25:
        grupo025 += 1
    if num >= 26 and num <= 50:
        grupo2650 += 1
    if num >= 51 and num <= 75:
        grupo5175 += 1
    if num >= 76 and num <= 100:
        grupo76100 += 1

print('-=' * 30)
print(f'Possuem {grupo025} numeros no grupo [0-25]')
print(f'Possuem {grupo2650} numeros no grupo [26-50]')
print(f'Possuem {grupo5175} numeros no grupo [51-75]')
print(f'Possuem {grupo76100} numeros no grupo [76-100]')
print('-=' * 30)