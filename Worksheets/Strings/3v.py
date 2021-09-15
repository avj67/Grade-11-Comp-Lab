for i in range (1,6):
    print("  "*(5-i), end = "")
    for j in range (i,2*i):
        print(j, end = " ")
    for k in range (j-1, i-1,-1):
        print(k,end = " ")
    print()
