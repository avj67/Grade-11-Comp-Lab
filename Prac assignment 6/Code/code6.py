# project details of employees

employees = {101:{1:["Banking",10], 2:["Etrade",3]}, 102:{1:["Banking",5], 3:["Ecommerce",15]}}
projectIds = {1:"Banking", 2:"Etrade", 3:"Ecommerce"}

# function to find employee with maximum experience
def maxProjExp():
    diSum = {}
    liMax = []
    liSums = []
    for code in employees:
        sum = 0
        for projCode in employees[code]:
            sum += employees[code][projCode][1]
        liSums.append(sum)
        diSum[sum] = code
    liSums.sort()
    maxSum = liSums[-1]
    liMax = [diSum[maxSum], maxSum]

    print(liMax[0], "-", liMax[1]//12, "years", liMax[1]%12, "months")

# function to add a new projec t detail or a new employee
def addProjDeets():
    code = int(input("Enter Employee code: "))
    print("Project codes:", projectIds)
    projCode = int(input("Enter project code: "))
    projExp = int(input("Enter project experience in months: "))
    if code not in employees.keys():
        employees[code] = {projCode:[projectIds[projCode], projExp]}
    else:
        employees[code][projCode] = [projectIds[projCode], projExp]

# function to show a employee experience in a project (tabular format)
def showTable():
    projCode = int(input("Enter project code: "))
    print("Project Name:", projectIds[projCode])
    print("Emp Code", " "*5, "Duration in months")

    # getting all keys from employees in a list to sort them
    empKeys = []
    for employee in employees:
        empKeys.append(employee)
    empKeys.sort()
    
    for i in range (len(empKeys)):
        print(empKeys[i], end= " "*(24-len(str(empKeys[i]))))
        
        if projCode not in employees[empKeys[i]]:
            employees[empKeys[i]][projCode] = [projectIds[projCode], 0]
            print(employees[empKeys[i]][projCode][1])
        else:
            print(employees[empKeys[i]][projCode][1])


print('''
1) Display employee code with maximum project experience in months and years.
2) Add additional project details for employees by providing employee code.
3) Accept project id and display employee code and duration of that employee in that project in tabular format
''')

restart = "y"
# rerun the code 
while restart == "y":
    choice = int(input("Choose option (1/2/3): "))

    if choice == 1:
        maxProjExp()
        restart = input("Restart (y/n): ")
        print()

    elif choice == 2:
        addProjDeets()
        restart = input("Restart (y/n): ")
        print()

    elif choice == 3:
        showTable()
        restart = input("Restart (y/n): ")
        print()

    else:
        print("ERROR: invalid option")
    

