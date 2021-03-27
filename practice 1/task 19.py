n = int(input())
letters = list(input())
print()
def FullPass(word):
    for let in letters:
        if  let not in word:
            return False
    return True

def StringCreate(word):
    if len(word) < n:
        for let in letters:
            StringCreate(word + let)
    elif FullPass(word):
        print(word)
StringCreate('')