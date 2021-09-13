row = int(input("Enter the number of rows:")) 

for i in range (1,row+1):  
    for j in range (0,i):  
      print(2**j, end = ' ')  

    for j in range (i-2,-1, -1):  
        print(2**j, end = ' ')
    print(' ')

    