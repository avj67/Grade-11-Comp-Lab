# pattern  

num = int(input("Input the number of rows:"))  
for i in range (1,num+1): 
    if (i%2==1): 
        for j in range (1,num): 
            if (j%2==1): 
                print("black",end='-') 

            else: 
                print("white",end='-') 

        if (num%2==1): 
            print("black") 

        else: 
            print("white") 
    else: 
         for j in range (1,num): 
            if (j%2==1): 
                print("white",end='-') 

            else: 
                print("black",end='-') 

         if (num%2==1): 
            print("white") 

         else: 
            print("black")

            