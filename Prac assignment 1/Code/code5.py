# script to display boiling point and freezing point of water in Fahrenheit

bp = input("Enter boiling point of water in Celsius: ")
fp = input("Enter freezing point of water in Celsius: ")

tempF = float(bp)*(9/5)+32
print("The boiling point of water is:", tempF, "F")

tempF = float(fp)*(9/5)+32
print("The freezing point of water is:", tempF, "F")

