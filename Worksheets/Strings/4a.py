sum = 0
n = 3
for i in range (2,2*n+1,2):
    if (i//2)%2 == 1:
        sum += i
    else:
        sum -= i
print(sum)