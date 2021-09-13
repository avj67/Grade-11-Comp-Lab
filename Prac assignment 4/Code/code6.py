# encrypting a string
str = input("Enter string: ").lower()
count = 0
for char in str:
    if char.isalpha():
        dummy = char
        if count == 0:
            char = char.replace(char, '!')
            print(char*(ord(dummy)-96), end = '')
            count += 1
        else:
            char = char.replace(char, '@')
            print(char*(ord(dummy)-96), end = '')
            count = 0
    else:
        print(char, end='')
        if count ==0:
            count += 1
        else:
            count = 0

