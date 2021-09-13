# script to find out hour in future

ch = int(input("Enter hour: ")) # getting current hour
timeIn = input("am (1) or pm (2): ")

if(timeIn=="1"):
    hAhead = int(input("How many hours ahead: ")) # getting the number of hours ahead
    if(ch==12 and hAhead<12):
        print("New Hour:", hAhead,"am")
    elif(ch==12 and hAhead>12):
        print("New Hour: ", hAhead, "pm")
    elif(ch+hAhead>=12):
        print("New Hour:", ch+hAhead-12,"pm")
    else:
        print("New Hour:", ch+hAhead,"am")

elif(timeIn == "2"):
    hAhead = int(input("How many hours ahead: ")) # getting the number of hours ahead
    if(ch==12 and hAhead<12):
        print("New Hour:", hAhead,"pm")
    elif(ch==12 and hAhead>12):
        print("New Hour: ", hAhead, "am")
    elif(ch+hAhead>=12):
        print("New Hour:", ch+hAhead-12,"am")
        
    else:
        print("New Hour:", ch+hAhead,"pm")

else:
    print("Enter valid number (1) or (2)")

