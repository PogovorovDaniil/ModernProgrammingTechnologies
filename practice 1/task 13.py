num = int(input())

isprime = True
i = 2
while isprime and i * i < num:
    if num % i == 0:
        isprime = False
    i += 1

if isprime:
    print('Простое')
else:
    print('Составное')