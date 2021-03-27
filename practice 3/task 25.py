import random, math

def BozoSort1(arr: list, order: bool = True):
    numlist = arr.copy()
    def Ordered():
        for i in range(len(numlist) - 1):
            if order and numlist[i] < numlist[i + 1]:
                return False
            if not order and numlist[i] > numlist[i + 1]:
                return False
        return True

    while not Ordered():
        r1 = random.randint(0, len(numlist) - 1)
        r2 = random.randint(0, len(numlist) - 1)
        if r1 == r2:
            continue
        numlist[r1] += numlist[r2]
        numlist[r2] = numlist[r1] - numlist[r2]
        numlist[r1] = numlist[r1] - numlist[r2]
        for num in numlist:
            print(num, end=' ')
        print()

def BozoSort2(arr: list[list], order: bool = True):
    numlist = []
    for row in arr:
        for num in row:
            numlist.append(num)
    BozoSort1(numlist, order)

def BozoSort3(a: int, b: int, c: int, order: bool = True):
    BozoSort1([a, b, c], order)

def ToIntList(obj: list) -> list:
    IntList = []
    for i in obj:
        IntList.append(int(i))
    return IntList

inp = input().split(' ')
if len(inp) == 1:
    n = int(inp[0])
    inp = input().split(' ')
    if len(inp) != n:
        for i in range(int(math.sqrt(n))-1):
            inp += input().split(' ')
    intList = ToIntList(inp)
    BozoSort1(intList)
    print()
    BozoSort1(intList, False)
elif len(inp) == 3:
    BozoSort3(int(inp[0]),int(inp[1]),int(inp[2]))
    print()
    BozoSort3(int(inp[0]),int(inp[1]),int(inp[2]), False)