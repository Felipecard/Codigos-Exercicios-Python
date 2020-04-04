
def notas(* notas, sit=0):
    dici = {}
    maior = cont = soma = 0

    for cada_nota in notas:
        if cada_nota > maior:
            maior = cada_nota
        soma += cada_nota
        cont += 1                 # Poderia usar o len(notas) aqui tambem
    media = soma / cont
    dici['Total'] = cont
    dici['Maior'] = maior
    dici['Menor'] = min(notas)    #Como ele fez o programa todo :( kkkk
    dici['Media da turma'] = media
    if sit == True:
        if media >= 7:
            dici['Situacao'] = 'BOA'

        elif media >= 5 and media < 7:
            dici['Situacao'] = 'RAZOAVEL'

        else:
            dici['Situacao'] = 'RUIM'
    return dici


# Main Program
resp = notas(7, 5, 3, 9, 5, 10, 9, sit=True)
print(resp)