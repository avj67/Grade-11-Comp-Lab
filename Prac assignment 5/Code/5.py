# print pattern

n = int(input("Enter n: "))
li = []

for num in range(n):
    li.append(num)

for i in range (len(li)):
    for j in range (i, len(li)):
        print(li[j], end = ' ')

    for k in range (i):
        print(li[k], end = ' ')
    
    print()

