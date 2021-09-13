cnt18=0
cnt25=0
cnt40=0
cnt55=0
cntMax=0

while(True):
    age=int(input("Enter age: "))
    if(age<=18):
        cnt18+=1
    elif(age>18 and age<=25):
        cnt25+=1
    elif(age>26 and age<=40):
        cnt40+=1
    elif(age>40 and age<=55):
        cnt55+=1
    elif(age>55):
        cntMax+=1

