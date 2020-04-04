print("-" * 30)
print("Sequencia Fibonacci")
print("-" * 30)
n = int(input("Quantos termos voce quer mostrar? "))

t1 = 0
t2 = 1
print("{} - {}".format(t1, t2), end = " ") #o END com VAZIO vai fazer que ele nao pule linha na hora de executar
print("~" * 30)
cont = 3

while(cont <= n):
    t3 = t1 + t2
    print(" - {}".format(t3), end = " ")
    t1 = t2
    t2 = t3
    cont = cont + 1
print("FIM")

