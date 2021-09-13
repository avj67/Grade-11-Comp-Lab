# all prime no.s upto n

upper = int(input("Enter upper range: "))  
  
for num in range(1,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
            print(num)
else:
    print("No prime numbers")

