# fibonacci series

n = int(input("Number of terms: "))
a = 0
b = 1
c = a+b
if n<2:
    print(a)
elif n<=2:
    print(a, b, end=' ')
elif n>2:
    print(a, b, c, end=' ')
    for i in range (3,n):
        a = b
        b = c
        c = a+b
        print(c, end=' ')
else:
    print("Error")

