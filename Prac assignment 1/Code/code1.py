import math
# script to evaluate certain values

r=10.51
b=4

#absolute value for (b-r)
abval=abs(b-r)
print("Absolute value:",abval)

#largest int not greater than (b-r)
c=b-r
print("Largest int not greater than (b-r):", math.floor(c))

#result of b<r
print ("b<r:", bool(b<r))

