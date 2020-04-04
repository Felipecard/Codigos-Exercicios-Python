
def voto(a):
    from datetime import date
    idade = date.today().year - a
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA!'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        idade >= 18
        return f'Com {idade} anos: VOTO OBRIGATORIO!'

# Main program
ano = int(input('Ano de nascimento: '))
print(voto(ano))