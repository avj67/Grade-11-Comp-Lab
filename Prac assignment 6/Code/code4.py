itemName = ["cake", "candy", "bread", "muffins", "pasta"]
itemStock = [20,45,40,25,12]
itemCost = [200, 45, 35, 25, 150]

itemInfo = list(zip(itemStock,itemCost))
shoplist = dict(zip(itemName, itemInfo))

def search():
    choice = "y"
    while choice == "y":
        print("-----------")
        item_searched = input("Find item: ")
        if item_searched.casefold() in shoplist:
            print(item_searched.capitalize(), "Found")
            print("Stock:",shoplist[item_searched][0])
            print("Price per unit:",shoplist[item_searched][1])
            choice = input("Search again (y/n): ")
        
        else:
            print(item_searched.capitalize(),"not found")
            choice = input("Search again (y/n): ")
    else:
        print("GoodBye!")

def rename():
    choice = "y"
    while choice == "y":
        print("-----------")
        item_searched = input("Rename item: ")
        if item_searched.casefold() in shoplist:
            print(item_searched.capitalize(), "Found")
            newName = input("Rename to: ")
            shoplist[newName] = shoplist[item_searched]
            del shoplist[item_searched]
            print(item_searched.capitalize(),"renamed to",newName.capitalize())
            print("Stock:",shoplist[newName][0])
            print("Price per unit:",shoplist[newName][1])
            choice = input("Run again (y/n): ")
        
        else:
            print(item_searched.capitalize(),"not found")
            choice = input("Run again (y/n): ")
    else:
        print("GoodBye!")

def minAndMax():
    for Key in shoplist:
        for altKey in shoplist:
            if shoplist[Key][1] < shoplist[altKey][1]:
                max = altKey.capitalize()
            if shoplist[Key][1] > shoplist[altKey][1]:
                min = altKey.capitalize()
    print("Item with maximum price per unit:", max)
    print("Item with minimum price per unit:", min)



    print("GoodBye!")

choice = input(
'''
a) Search for an item and if available, display item name, stock and price per unit.
b) Rename an item in the same dictionary.
c) Display the item with minimum and maximum price per unit

Choice: ''')

if choice == "a":
    search()

if choice == "b":
    rename()

if choice == "c":
    minAndMax()

