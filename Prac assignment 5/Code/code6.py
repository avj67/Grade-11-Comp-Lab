# menu driven python code

master_li = []
reward_li=[] # dummy data...can be edited
count = 0
restart = "y"

# when option 1 selected
def addReward():
    rew_choice = int(input("Enter roll no.: "))
    reward_li.append(rew_choice)

# when option 3 selected
def report():
    print(
'''
Roll no.            Name            No.of rewards
''')

    for i in range(len(master_li)):
        print(master_li[i][0], end=' '*(20-len(str(master_li[i][0]))))
        print(master_li[i][1], end=' '*(21-len(master_li[i][1])))
        print(reward_li.count(i+1))

...

# Home
print(
'''
=======================================
#               WELCOME               #
#               *******               #
#    (1) Reward a student             #
#    (2) Add a new student            #
#    (3) See Report                   #
=======================================
'''
)

# runs till user is done
while restart == "y":
    choice = int(input("Pick option (1) or (2) or (3): "))

    if choice == 1:
        addReward()
        restart = input("Restart (y/n): ")
        print()

    elif choice == 2:
        name = input("Enter name: ")
        count += 1
        newStudent_li = [count,name]
        master_li.append(newStudent_li)
        restart = input("Restart (y/n): ")

    elif choice == 3:
        report()
        restart = input("Restart (y/n): ")
        
    else:
        print("Invalid option")

# when user is done
else:
    print('''
------------------------------------------
                GoodBye!
''')
