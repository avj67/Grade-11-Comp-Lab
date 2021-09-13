# code to arrange numbers in descending order

n1 = int(input("Enter a num: "))
n2 = int(input("Enter a num: "))
n3 = int(input("Enter a num: "))

max = n1
min = n1

if (max>n2):
    max = n1
    min = n2
    if(min<n3):
        mid = n3
    else:
        mid = n2
        min = n3

if(n2>max):
    max = n2
    min = n1
    if(min<n3):
        mid = n3
    else:
        mid = n1
        min = n3

if (max>n3):
    max = n1
    min = n3
    if(min<n2):
        mid = n2
    else:
        mid = n3
        min = n2

if(n3>max):
    max = n3
    min = n1
    if(min<n2):
        mid = n2
    else:
        mid = n1
        min = n2

else:
    print("Invalid no.s")
print (max,mid,min)

