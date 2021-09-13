# script to find total resistance of 2 resistors

# obtaining the input
res1 = float(input("Resistance of resistor 1: ")) 
res2 = float(input("Resistance of resistor 2: "))

# type of arrangement
arr = input("Which type of arrangement is this(s/p): ")

# calculating total resistance
if(arr=="s"):
    print("Total resistance in series is",(res1+res2))
elif(arr=="p"):
    print("Total resistance in parallel is", res1*res2/(res1+res2))
else:
    print("Enter valid arrangement")
