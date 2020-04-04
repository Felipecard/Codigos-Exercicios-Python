print("SEU PESO IDEAL")

sexo = input("Voce é homem ou mulher? (H) ou (M)")
sexo = sexo.upper()

altura = float(input("Qual sua altura?"))

if(sexo == "H"):
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal seria {}!".format(peso_ideal))
elif(sexo == "M"):
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal seria {}!".format(peso_ideal))

