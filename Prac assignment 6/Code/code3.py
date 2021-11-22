di = {}
word = input("Enter word: ")

for ch in word:
    if ch in di.keys():
        di[ch] += 1
    else:
        di[ch] = 1
print(di)

