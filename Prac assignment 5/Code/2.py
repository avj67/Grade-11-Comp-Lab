# check if sum of cubes of its digits is equal to the number

n = int(input("How many nums: "))
li = []
count = 0

for i in range(n):
    num = int(input("Input: "))
    li.append(num)

print("Armstrong nums: ",end='')
for j in range (n):
    num = li[j]
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        count+=1
        print(num, end=' ')
if count == 0:
        print("none found")


