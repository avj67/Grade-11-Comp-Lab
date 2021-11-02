# Accept nums from user and display longest sequence of odd numbers as a tuple

li = []
count = 0
li_temp = []
li_new=[]
li_final = []

n = int(input("How many nums: "))

# accept input
for i in range(n):
    num = int(input("Input: "))
    li.append(num)
t = tuple(li)

for j in range(n):
    if t[j]%2 == 1:
        li_new.append(t[j])
        temp_count = 1
        count += 1
        if temp_count>=count:
            li_final=li_new

# reset values if num is even
    else:
        temp_count = count
        li_temp=li_new
        li_new=[]
        count=0

print ("input:",t)
print("Longest sequence of odd numbers in the tuple:",tuple(li_final))
