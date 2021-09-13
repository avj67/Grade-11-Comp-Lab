# replace all vowels in string with '*'
str_og = input("Enter a string: ")
str_mod = ''
vow = 'aeiouAEIOU'
for char in str_og:
    if char in vow:
        str_mod = str_mod+'*'
    else:
        str_mod = str_mod + char
print (str_mod)

