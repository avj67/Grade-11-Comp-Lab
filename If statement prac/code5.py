# script to toggle case of the input

print (ord("a")) # getting the unicode value of "a"
print (ord("z")) # getting the unicode value of "z"

str = str(input("Enter a letter: "))

if (ord(str) >= 97 and ord(str) <= 122): # setting the range
    print("Letter in uppercase:", str.upper())
else:
    print("Letter in lowercase:", str.lower())

