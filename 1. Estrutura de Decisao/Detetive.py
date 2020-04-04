
print("DETETIVE")

p1 = input("Telefonou para a vitima?")
p2 = input("Esteve no local do crime?")
p3 = input("Mora perto da vítima?")
p4 = input("Devia para a vítima?")
p5 = input("Já trabalhou com a vítima?")

if(p1 == "sim"):
    s1 = 1
else:
    s1 = 0
if(p2 == "sim"):
    s2 = 1
else:
    s2 = 0
if(p3 == "sim"):
    s3 = 1
else:
    s3 = 0
if(p4 == "sim"):
    s4 = 1
else:
    s4 = 0
if(p5 == "sim"):
    s5 = 1
else:
    s5 = 0

soma = s1 + s2 + s3 + s4 + s5
print(soma)

if(soma == 5):
    print("ASSASSINO")
elif(soma < 5 and soma > 2):
    print("SUSPEITO")
elif(soma < 2):
    print("INOCENTE")

