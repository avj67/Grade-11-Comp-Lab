# replace elements of list greater than 100 with 100

li = [100,1,2,3,4,123,453,98,45,67,233]
li_edited = li
min = None
max = None
max2 = None

for i in range (len(li)):

    # making all nums > 100 eqqual to 100
    if li_edited[i] > 100:
        li_edited[i] = 100

    # min
    for j in range (len(li)):
        if li[j] < li[i]:
            min = li[j]
            break

    # largest
    for j in range (0,len(li)):
        if li[j] > li[i]:
            max = li[j]
            break
    
    # 2nd largest
    for k in range (len(li)):
        if li[k] > li[i] and li[k] < max:
            max2 = li[k]
            break
            

print(li)
print("min:", min)
print("Largest num:", max)
print("Second largest num:", max)
