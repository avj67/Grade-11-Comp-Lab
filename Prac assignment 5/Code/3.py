# Accept nums from user and display longest sequence of odd numbers as a tuple

longest = []
current = []
nums_li = []
n = None

while n != -1:
    n = int(input("Enter num: "))
    nums_li.append(n)

    if current and current[-1] % 2 == 1:
        current.append(n)
    else:
        current = [n]

    if len(current) > len(longest):
        longest = current
else:
    del longest[-1]

nums_tup = tuple(nums_li)
print(nums_tup)
print(tuple(longest))

