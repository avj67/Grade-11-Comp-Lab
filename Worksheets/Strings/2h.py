st = "Assassination"
st2=""
for i in range (len(st)):
    if st[i].casefold().find(st[i],i+1,len(st)):
        if st[i].casefold() not in st2.casefold():
            st2 = st2 + st[i]
print(st2)