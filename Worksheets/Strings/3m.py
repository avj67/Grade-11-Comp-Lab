rows = 4
count = 1
for i in range (1,3*rows+1):
    if count <= 3:
        print (i, end = " ")
        count += 1
    else:
        print()
        print(i, end = " ")
        count = 2
