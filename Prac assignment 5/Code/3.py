# Accept nums from user and display longest sequence of odd numbers as a tuple

longest = []
current = []
n = None

while n != -1:
    n = int(input("Enter num: "))

    if current and current[-1] % 2 == 1:
        current.append(n)
    else:
        current = [n]

    if len(current) > len(longest):
        longest = current
else:
    del longest[-1]

print(longest)
