# srcipt for finding no. of days A, B, C will take to complete work together

x = float(input("No. of days A takes: ")) # Days required by A
y = float(input("No. of days B takes: ")) # Days required by B
z = float(input("No. of days C takes: ")) # Days required by C

days = x*y*z/(x*y+y*z+x*z)
format_days = "{:.2f}".format(days)
print("No. of days consumed when A, B and C work together:", format_days) # Days consumed when A, B, C work together


