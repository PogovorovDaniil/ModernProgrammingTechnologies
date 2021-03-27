num = int(input())
pow = int(input())

answer = 1
if pow > 0:
    answer = num
    for _ in range(pow - 1):
        answer *= num
elif pow < 0:
    answer = 1.0 / num
    for _ in range(- 1 - pow):
        answer /= num

print(answer)