# print pattern

n = int(input("Enter a number: ")) 
outer_li = [] 
row = 0 
inner_li = [] 

for i in range (n): 
    j = i 
    for j in range (i, n): 
        inner_li.append(j) 
    for j in range (i): 
        inner_li.append(j) 
    outer_li.append(inner_li) 
    inner_li = [] 

for i in range (len(outer_li)): 
    for j in range (len(outer_li[i])): 
        print (outer_li[i][j], end = ' ') 
    print ("")