def NOK():
    while True:
        try:
            a = int(input())
            b = int(input())
        except ValueError:
            print("Ошибка! Нужно ввести два натуральных числа.")
            continue
        if a < 1 or b < 1:
            print("Числа должны быть положительными.")
            continue
        break
    m = max(a, b)
    step = m
    while True:
        if m % a == 0 and m % b == 0:
            return m
        m += step

print("Последовательно введите 2 числа чтобы высчитать их НОК")
print(NOK())