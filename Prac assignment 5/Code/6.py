# menu driven python code

master_li = [[1,'Ajay'],[2,"Rohit"],[3,'Suresh'],[4,'Mukesh'],[5,'Anish'],[6,'Karthik'],[7,'Sunil'],[8,'Manish'],[9,'Hemali'], [10, 'Tiara']]
reward_li=[1,1,2,3,4,2,5,1,5,9,7,6] # dummy data...can be edited
count = 0
restart = "y"

# when option 1 selected
def addReward():
    rew_choice = int(input("Enter roll no.: "))
    reward_li.append(rew_choice)

# when option 2 selected
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
#    (1) Add value to rewards list    #
#    (2) See Report                   #
=======================================
'''
)

# runs till user is done
while restart == "y":
    choice = int(input("Pick option (1)/(2): "))

    if choice == 1:
        addReward()
        restart = input("Restart (y/n): ")
        print()

    elif choice == 2:
        report()
        restart = input("Restart (y/n): ")
        print()
        
    else:
        print("Invalid option")

# when user is done
else:
    print("GoodBye!")
