numbers = [0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0]
colors =  (0, 1,2,1, 2,1,2, 1,2,1, 2,2,1, 2,1,2, 1,2,1, 1,2,1, 2,1,2, 1,2,1, 2,2,1, 2,1,2, 1,2,1)

redCount = 0
blackCount = 0

while True:
    num = int(input())
    if num < 0:
        break
    if num < 37:
        numbers[num] += 1
        if colors[num] == 1:
            redCount += 1
        elif colors[num] == 2:
            blackCount += 1

    for i in range(len(numbers)):
        if numbers[i] > 0:
            print(i,end=' ')
    print()
    for i in range(len(numbers)):
        if numbers[i] == 0:
            print(i,end=' ')
    print()
    print(redCount, blackCount)
    print()