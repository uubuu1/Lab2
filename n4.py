def ex1():
    while True:
        try:
            a = int(input())
        except:
            print("ЦЕЛОЕ ЧИСЛО.")
            continue
        break
    print("Успешная попытка!")

def ex2():
    while True:
        try:
            a = int(input())
        except:
            print("Отлично! Обнаружив ошибку, сработал except.")
            break
        print("Отличный ввод, но сейчас нужно нарочно допустить ошибку в нём.")

def ex3():
    c = 0
    try:
        a=int(input())
    except:
        c = 1
    finally:
        if c == 0:
            print("Введено целое число. Это вам говорит print из finally.")
        else:
            print("Ввод не является целым числом. Это вам говорит print из finally.")

print("Демонстрация работы try / except / finally")
print("Введите целое число:")
ex1()
print("Теперь давайте введём некорректные данные на прошлый запрос - ввести целое число:")
ex2()
print("А сейчас посмотрите на finally. Он не требует от вас выполнения определённых условий, просто послушно выполняет свою работу.")
ex3()