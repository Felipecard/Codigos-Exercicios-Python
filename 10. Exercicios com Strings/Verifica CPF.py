
cpf = str(input('CPF: '))

try:
    int(cpf[0])
    int(cpf[1])
    int(cpf[2])
    int(cpf[4])
    int(cpf[5])
    int(cpf[6])
    int(cpf[8])
    int(cpf[9])
    int(cpf[10])
    int(cpf[12])
    int(cpf[13])
    if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
        print('CPF VALIDO! :)')
    else:
        print('CPF Invalido')
except:
    print('CPF Invalido')

