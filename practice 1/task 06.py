import math

a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4 * a * c
if a != 0:
    if D > 0:
        print('\tx1 =', (-b + math.sqrt(D)) / (2 * a))
        print('\tx2 =', (-b - math.sqrt(D)) / (2 * a))
    elif D == 0:
        print('\tx =', -b / (2 * a))
    else:
        print('\nДействительных корней нет')
else:
    print('\tx =', -c / b)