
cont = 1
total_eleitores = int(input("Quantos candidatos participaram dessa eleicao?"))
numero_eleitor = 1
lista_votos = []
a = 0
while(cont <= total_eleitores):
    voto = (input("Diga o voto do candidato{}: (A) --> Geremias. (B) --> Lila. (C) --> Gogos".format(numero_eleitor)))
    lista_votos.append(voto)
    cont += 1
print(lista_votos)

a = 0
b = 0
c = 0
for voto in lista_votos:
    if(voto == "a"):
        a = a + 1
    elif(voto == "b"):
        b = b + 1
    elif(voto == "c"):
        c = c + 1
print("Votos no Geremias:", a)
print("Votos na Lila:", b)
print("Votos no Gogos:", c)

