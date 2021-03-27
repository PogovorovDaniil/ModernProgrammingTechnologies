g = 9.8

inp = input().split(' ')
x0 = float(inp[0])
v0 = float(inp[1])
t = float(inp[2])
x = x0 + v0 * t + g * t**2 / 2
print(x)