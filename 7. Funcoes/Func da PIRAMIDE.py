
def piramide(l):
    n = l + 1
    o = 1
    for k in range(1, n):
        if k == 1:
            print(k)
        if k > 1:
            for h in range(k, o + k):
                print(k, end='   ')
            print()
        o += 1


# Main
l = int(input('Qual valor de n? '))
piramide(l)
