diff = 4
for i in range (1,6):
    num = i
    for j in range (1,i+1):
        print (num,end = ' ')
        num += diff
        diff -= 1
    diff = 4
    print()