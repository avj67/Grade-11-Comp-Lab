# Accept nums from user and display longest sequence of odd numbers as a tuple

longest = []
current = []

while True:
    n = int(input("Enter num: "))
    if n == -1:
        del longest[-1]
        break

    if current and current[-1] % 2 == 1:
        current.append(n)
    else:
        current = [n]

    if len(current) > len(longest):
        longest = current
print(longest)
