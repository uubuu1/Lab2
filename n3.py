def init(a, b):
    matr = []
    for i in range(a):
        line = []
        for j in range(b):
            if (i + j) % 2 == 1:
                line.append("*")
            else:
                line.append(".")
        matr.append(line)
    return matr

def printMatr(matr):
    for i in range(0, len(matr)):
        for j in range(0, len(matr[i])):
            print(matr[i][j], end=' ')
        print()

print("Введите поочерёдно два числа, задающих размерность массива")
while True:
    try:
        a = int(input())
        b = int(input())
    except ValueError:
        print("Необходимо ввести два натуральных числа")
        continue
    if a < 1 or b < 1:
        print("Числа должны быть больше нуля")
        continue
    break
matr = init(a,b)
printMatr(matr)