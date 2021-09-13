# script to generate bill based on units of elec consumed

name = input("Customer Name: ")
units = int(input("No. of units: "))

if(units<100):
    bill = units*3

elif(units>100 and units<=150):
    bill = units%100*5 + 100*3

else:
    bill = (units-150)*7 + 100*3 + 50*5

print("Total Bill:","Rs.",bill)

