n = int(input())
k = int(input())

alkos = []

for _ in range(k):
    inp = input().split(' ')
    alkos.append([inp[0], int(inp[1]), int(inp[2])])

for alko in alkos:
    alko.append(alko[2] / alko[1])

toBuy = []

def SetAlkos(n):
    minalko = ['none', n + 1, 0, 0]
    for alko in alkos:
        if alko[3] > minalko[3] and alko[1] <= n:
            minalko = alko
    if minalko[1] > n:
        return
    count = int(n / minalko[1])
    toBuy.append((minalko[0], count))
    n -= count * minalko[1]
    SetAlkos(n)
SetAlkos(n)

print(toBuy)