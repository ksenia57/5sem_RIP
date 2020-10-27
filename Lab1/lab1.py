import sys
from math import sqrt

print("ИУ5-52Б Рабцевич Ксения")

def count(a, b, c):
    if a == 0:
        v1 = -c/b
        if v1 < 0:
            print("Нет корней")
        elif v1 == 0:
            print("x1 = 0")
        else:
            x1 = sqrt(v1)
            x2 = -sqrt(v1)
            print('x1 = {}, x2 = {}'.format(x1, x2))

    if b == 0:
        v2 = -c/a
        if v2 < 0:
            print("Нет корней")
        elif v2 == 0:
            print("x1 = 0")
        else:
            x1 = sqrt(sqrt(v2))
            x2 = -sqrt(sqrt(v2))
            print("x1 = {}, x2 = {}".format(x1, x2))

    else:
        D = pow(b, 2) - (4 * a * c)
        if D < 0:
            print("Нет корней")
        else:
            y1 = ((-b - sqrt(D)) / (2 * a))
            y2 = ((-b + sqrt(D)) / (2 * a))
            k=1
            if (y1!=y2):
                if y1 > 0:
                    x1 = sqrt(y1)
                    x2 = -sqrt(y1)
                    print("x1 = {}, x2 = {}".format(x1, x2))
                    k+=2
                elif y1==0:
                    print("x1 = 0")
                    k+=1

            if y2 > 0:
                x1 = sqrt(y2)
                x2 = -sqrt(y2)
                print("x{} = {}, x{} = {}".format(k, x1, k+1, x2))
            elif y2 == 0:
                print("x{} = 0".format(k))

text = "Коэффициент введён неправильно, попробуйте снова"
if len(sys.argv) == 4:
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    except:
        print("Неправильно введены коэффициенты")
        exit()
else:
    print ("Введите коэффициенты a, b и c")
    while 1:
        try:
            a = float(input())
            break
        except:
            print(text)
    while 1:
        try:
            b = float(input())
            break
        except:
            print(text)
    while 1:
        try:
            c = float(input())
            break
        except:
            print(text)
if a == 0 and b == 0 and c == 0:
    print("Бесконечное число корней")
elif a == 0 and b == 0:
    print("Корней нет")
else:
    count(a,b,c)