Marks={}
toppers = []
n = int(input("Enter num of students: "))
for i in range (n):
    name = input("Name: ")
    marks = int(input("Marks: "))
    print()
    Marks[i] = [name, marks]

    if marks > 75:
        toppers.append(name)

print("Students with marks > 75:",end=" ")
for topper in toppers:
     print(topper, end=", ")

