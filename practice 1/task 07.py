import math

inputType = input()
if inputType == '1':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2

    print('S =', math.sqrt(p * (p - a) * (p - b) * (p - c)))
elif inputType == '2':
    xy1 = input()
    x1 = float(xy1.split(' ')[0])
    y1 = float(xy1.split(' ')[1])
    
    xy2 = input()
    x2 = float(xy2.split(' ')[0])
    y2 = float(xy2.split(' ')[1])

    xy3 = input()
    x3 = float(xy3.split(' ')[0])
    y3 = float(xy3.split(' ')[1])

    print('S =', ((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)) / 2)
else:
    print('Вы ввели некорректное значение действия!')