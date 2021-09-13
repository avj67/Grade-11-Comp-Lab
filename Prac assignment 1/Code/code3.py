# script to display refund received for returning containers

contNo=input("No. of containers of capacity <=1: ")
contNo2=input("No. of containers of capacity >1: ")

refund=int(contNo)*0.10+int(contNo2)*0.25

# formatting the output
format_refund = "{:.2f}".format(refund)
print("Your refund for the containers is:", format_refund,"$")
