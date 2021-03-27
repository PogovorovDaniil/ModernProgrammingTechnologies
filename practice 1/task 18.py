words = ['hallo', 'klempner', 'das', 'ist', 'fantastisch', 'fluggegecheimen']

letters = {}
countLetters = 0

for let in range(97, 123):
    letters[chr(let)] = 0

for word in words:
    for let in word:
        letters[let] += 1
        countLetters += 1

stopWord = input()

p = 1
for let in stopWord:
    p *= letters[let] / countLetters

print(p)