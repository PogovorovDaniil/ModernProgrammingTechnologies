import random

print('{Приветственное сообщение от игры}')
while True:
    rnum = random.randint(1, 100)
    for i in range(5):
        num = int(input('Введите целое число: '))
        if num < rnum:
            print('Загаданное число больше чем', num)
        elif num > rnum:
            print('Загаданное число меньше чем', num)
        else:
            print('Поздравляю! Вы угадали')
            break
        if i == 4:
            print('Вы проиграли. Было загадано:', rnum)
    next = int(input('Хотите начать сначала? (1 - ДА ): '))
    if next != 1:
        break