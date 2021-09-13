# check if he entered year is a leap year or not

y = int(input("Enter the year:")) 
if (y%100==0): 
    if(y%400==0): 
        print("It is a leap year") 
    else: 
        print("It is not a leap year") 
elif (y%4==0): 
    print("It is a leap year") 
else: 
    print("Wrong input") 

