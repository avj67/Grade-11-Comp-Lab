# wap to input 10 int and stop if no. is divisible by 7

tot = 0
cv = 1
while(cv<=10):
    num = int(input("Enter a no.: "))
    if(num%7==0):
        break
    tot+=num
    cv+=1
print("The sum of no. is: ", tot)
