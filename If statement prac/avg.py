cnt=0
sum=0
while (True):
    n=int(input("num: "))
    sum+=n
    cnt+=1
    cont=input("Continue yes(1) or no(2):")
    if(cont==2):
        break
avg=sum/cnt
print("Avg=",avg)