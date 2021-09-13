# script to find which quadrant the point lies in

x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))

if(x>0 and y>0):
    print("(",x,",",y,") ","lies in quad I", sep="")
elif(x<0 and y>0):
    print("(",x,",",y,") ","lies in quad II", sep="")
elif(x<0 and y<0):
    print("(",x,",",y,") ","lies in quad III", sep="")
else:
    print("(",x,",",y,") ","lies in quad IV", sep="")

