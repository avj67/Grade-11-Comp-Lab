# first 15 terms of fibonacci series 

a=0
b=1
c=a+b

print(a, end=',')
print(b, end=',')
print(c, end=',')

for i in range (0,12,1):
    a=b
    b=c
    c=a+b
    print(c, end=',')

