# script to find if dart hits dartboard

x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))

dist = pow(pow(x,2)+pow(y,2),1/2)
rad = 10

if(dist<=rad):
    print("Hit")
    print("Distace from center:",dist)
else:
    print("Miss")

