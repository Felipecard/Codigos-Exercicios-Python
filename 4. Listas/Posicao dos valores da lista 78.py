
num = []

for n in range(0, 5):
    num.append(int(input('Digite um valor...')))

max = max(num)
min = min(num)

for c, v in enumerate(num):
    print(f'O valor {v}, esta na posicao {c}')
    
print(max)
print(min)
