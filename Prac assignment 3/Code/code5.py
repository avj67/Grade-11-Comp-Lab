# series
import math
n = int(input("Enter n: "))
x = int(input("Enter x: "))
sum = 0
count = 1
for i in range (1,n+1):
    if i%2==0:
        sum += math.pow(x,i)/math.factorial(i)
    else:
        sum -= math.pow(x,i)/math.factorial(i)
    
print (sum, "is the sum")

