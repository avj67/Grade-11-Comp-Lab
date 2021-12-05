di = {}
word = input("Enter word: ")
choice = "y"

while choice == "y":
    for ch in word:
        if ch in di.keys():
            di[ch] += 1
        else:
            di[ch] = 1
    print(di) 
    choice = input("Repeat: ")


