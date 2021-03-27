import math

num = int(input())

if num > 1:
    print(math.ceil(math.log2(num)))
else:
    print(num)