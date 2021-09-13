n = 4
for row in range (1,n+1):
    for i in range (n-row+1):
        print(" ", end = " ")
    for num in range (row,0,-1):
        print(num, end = " ")
    for num in range (2,row+1):
        print(num, end = " ")
    print()