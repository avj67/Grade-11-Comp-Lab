# check for perfect no.

sum = 0
num = int(input("Enter num: "))

if (num>0):
    for i in range (1,int(num/2+1)):
        if (num%i==0):
            sum += i
    if (sum==num):
        print(num,"is a perfect no.")
    else:
        print(num, "is not a perfect num")
else:
    print('''Error!
Number must be a positive integer''')

