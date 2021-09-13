# min no. of notes
count=0
amt=int(input("Amount: "))

while 500<=amt:
    count+=1
    amt=amt-500
if count!=0:
    print("500:",count)
count=0

while 50<=amt:
    count+=1
    amt=amt-50
if count!=0:
    print("50:",count)
count=0

while 20<=amt:
    count+=1
    amt=amt-20

if count!=0:
    print("20:",count)
count=0

while 5<=amt:
    count+=1
    amt=amt-5
if count!=0:
    print("5:",count)
count=0

while 2<=amt:
    count+=1
    amt=amt-2
if count!=0:
    print("2:",count)
count=0

while 1<=amt:
    count+=1
    amt=amt-1
if count!=0:
    print("1:",count)
count=0
