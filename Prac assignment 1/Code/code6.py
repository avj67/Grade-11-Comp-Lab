# To find the ht reached by the ladder on the wall 
import math

length = float(input("Enter length of the ladder in feet:"))  
angle_degrees = float(input("Enter the angle in degrees:"))  
angle_rad = (math.pi/180)*angle_degrees

ht = (length * math.sin(angle_rad))  
format_ht = ("The ht reached by the ladder on the wall is: {:.2f}".format(ht))

print (format_ht)

