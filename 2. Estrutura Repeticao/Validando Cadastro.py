
print("VALIDANDO CADASTRO")

nome = input("Nome de usuario:")
while(len(nome) < 3):
    nome = input("O nome precisa conter mais de 3 caracteres, coloque novamente:")

idade = int(input("Idade:"))
while(idade < 0 or idade > 150):
    idade = int(input("A idade precisa ser maior que 0, coloque novamente:"))

salario = float(input("Salario:"))
while(salario < 0):
    salario = float(input("O salario precisa ser maior que 0, insira novamente:"))

sexo = input("Sexo... (H) ou (M):")
sexo = sexo.upper()
while(sexo != "M" and sexo != "H"):
    sexo = input("Só sao aceitas as ltras M ou H, coloque novamente:")
    sexo = sexo.upper()

estado_civil = input("Estado Civil...(S) ou (C) ou (V) ou (D):")
estado_civil = estado_civil.upper()
while(estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D"):
    estado_civil = input("Só sao aceitas as ltras (S) ou (C) ou (V) ou (D), coloque novamente:")
    estado_civil = estado_civil.upper()

print("---------------------------------")
print("Cadasto feito, confira os dados")
print("Nome:", nome)
print("Idade:", idade)
print("Salario: R$", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)
print("---------------------------------")