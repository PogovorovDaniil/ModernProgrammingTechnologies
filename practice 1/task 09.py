firstTime = input()
h1 = int(firstTime.split(':')[0])
m1 = int(firstTime.split(':')[1])
if h1 < 0 or h1 > 23:
    raise Exception('Часы должны находиться в промежутке [0, 23]')
if m1 < 0 or m1 > 59:
    raise Exception('минуты должны находиться в промежутке [0, 59]')

secondTime = input()
h2 = int(secondTime.split(':')[0])
m2 = int(secondTime.split(':')[1])
if h2 < 0 or h2 > 23:
    raise Exception('Часы должны находиться в промежутке [0, 23]')
if m2 < 0 or m2 > 59:
    raise Exception('Минуты должны находиться в промежутке [0, 59]')

absM1 = h1 * 60 + m1
absM2 = h2 * 60 + m2

difference = absM1 - absM2
if difference < 0:
    difference = -difference

if difference <= 15:
    print('Встреча состоится')
else:
    print('Встреча не состоится')
