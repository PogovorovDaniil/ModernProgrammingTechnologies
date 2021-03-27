import re

regex = re.compile('\\w\\w\\d{7}')
regexSuslik = re.compile('a\\w\\d\\d55661')

input()#Потому что задание...
tickets = input().split(' ')
for ticket in tickets:
    if not regex.fullmatch(ticket):
        print(ticket, 'не подходит по формату!')
        continue
    if regexSuslik.fullmatch(ticket):
        print(ticket)
    