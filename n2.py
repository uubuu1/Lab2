def sg():
    a = []
    print("Введите количество элементов списка")
    while True:
        try:
            l = int(input())
        except:
            print("В содержимом ввода присутствует ошибка, повторите попытку.")
            continue
        break
    print("Последовательно введите список целых чисел")
    for i in range(l):
        while True:
            try:
                a.append(int(input()))
            except:
                print("В содержимом ввода присутствует ошибка, повторите попытку.")
                continue
            break
    s = 1
    c = []
    print("Уникальные элементы списка:")
    for i in range(l):
        if a[i] not in c:
            print(a[i], end=' ')
            c.append(a[i])
        s *= a[i]
    print()
    print("Среднее геометрическое чисел", s ** (1.0/l))

def ks():
    d = dict()
    print("Введите количество элементов словаря:")
    while True:
        try:
            l = int(input())
        except:
            print("В содержимом ввода присутствует ошибка, повторите попытку.")
            continue
        break
    print("Последовательно введите словарь в порядке значение, ключ")
    for i in range(l):
        d[input()] = input()
    k = list(d.keys())
    print("Список ключей словаря:")
    for i in range(l):
        print(k[i], end=' ')

def rzr():
    print("Введите число:")
    while True:
        try:
            num = int(input())
        except:
            print("В содержимом ввода присутствует ошибка, повторите попытку.")
            continue
        break
    r = 1
    while num > 9:
        num /= 10
        r += 1
    print("Разряд у введённого числа равен", r)

def pal():
    print("Введите строку")
    s = str(input())
    w = ""
    answ = 0
    for i in range(len(s)):
        if s[i] == ' ' or i == len(s) - 1:
            if i == len(s) - 1:
                w += s[i]
            answ += 1
            for j in range(len(w) // 2):
                if w[j] != w[len(w) - j - 1]:
                    answ -= 1
                    break
            w = ""
        else:
            w += s[i]
    print("Количество палиндромов в строке составляет", answ)

while True:
    print("Что вы хотите сделать?\n1 - найти уникальные элементы и среднее геометрическое числовой последовательности\n2 - получить все ключи словаря\n3 - посчитать количество разрядов числа\n4 - посчитать количество палиндромов строки.")
    try:
        choice = int(input())
    except:
        print("Нужно ввести число, соотвествующее одному варианту из представленных. Повторите попытку.")
    else:
        if choice not in [1,2,3,4]:
            print("Нужно ввести число, соотвествующее одному варианту из представленных. Повторите попытку.")
        elif choice == 1:
            sg()
        elif choice == 2:
            ks()
        elif choice == 3:
            rzr()
        else:
            pal()
    break
