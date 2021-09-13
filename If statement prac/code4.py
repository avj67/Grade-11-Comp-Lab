# script to find largest number

# getting the numbers from the user
num1 = input("Enter a num: ")
num2 = input("Enter a num: ")
num3 = input("Enter a num: ")
num4 = input("Enter a num: ")

dummy=num1

# running the conditional statements
if(num1>num2):
    dummy=num1
    if(dummy>num3):
        dummy=num1
        if(dummy>num4):
            print("Largest no.:", dummy)
        else:
            dummy=num4
            print("Largest no.:", dummy)
    else:
        dummy=num3
        if(dummy>num4):
            print("Largest no:", dummy)
        else:
            dummy=num4
            print("Largest no:", dummy)
            
else:
    dummy=num2
    if(dummy>num3):
        dummy=num2
        if(dummy>num4):
            print("Largest no.:", dummy)
        else:
            dummy=num4
            print("Largest no.:", dummy)
    else:
        dummy=num3
        if(dummy>num4):
            print("Largest no:", dummy)
        else:
            dummy=num4
            print("Largest no:", dummy)

