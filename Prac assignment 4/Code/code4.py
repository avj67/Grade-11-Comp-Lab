# display rotated version of string
str_og = input("Enter a string: ")
n = int(input("Enter n: "))
str_mod = str_og[n:]+str_og[0:n]
print (str_mod)

