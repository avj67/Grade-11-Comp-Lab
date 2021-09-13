# program to print avg of digits or the no. of consonents in string
string= input("Enter a string:")
tot = 0
vow = "aeiouAEIOU"
count = 0
for i in string:
    if(i.isdigit()):
        tot+= int(i)
        count += 1
if count!=0:
    print("The average of the number of digits are: ",(tot/count))
count=0
for i in string:
    if(i.isalpha()):
        if(i not in vow):
            count +=1
print("The number of consonents are: ",count)

