inp = input().split(' ')
s = int(inp[0])
l1 = int(inp[1])
r1 = int(inp[2])
l2 = int(inp[3])
r2 = int(inp[4])

if s > l1 + l2 or s < r1 + r2:
    if r1 - l1 > r2 - l2:
        print(s - r2, r2)
    else:
        print(l1, s - l1)
else:
    print('-1')