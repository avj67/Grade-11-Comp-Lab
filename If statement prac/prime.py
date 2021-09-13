# script to print all prime facbers between 2 facbers inputed by the user

n1 = int(input("Enter n1: "))  
n2 = int(input("Enter n2: "))  
  
for fac in range(n1,n2 + 1):  
   if fac > 1:  
       for i in range(2,fac):  
           if (fac % i) == 0:  
               break  
       else:  
           print(fac)

