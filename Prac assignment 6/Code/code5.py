# print key value with most unique digits

# input
di = {"One" : [5, 7, 9, 7, 0], "Two" : [6, 7, 4, 3, 3], "Three" : [9, 9, 6, 5, 5]}
# keeps track of count of each digit in a key
tracker = {}

# list used later to find max value
li_unique = []
# dictionary containing key and number of its unique digits
di_unique = {}

for key in di:
    tracker[key] = {}
    for num in di[key]:
        tracker[key][num] = 0
        for othrNum in di[key]:
            if othrNum == num:
                tracker[key][num] += 1

print("Input:", di)

for key in tracker:
    
    # finding number of unique digits in the key
    numOfUnique = 0
    length = len(tracker[key].keys())
    for subKey in tracker[key]:
        if tracker[key][subKey] == 1:
            numOfUnique += tracker[key][subKey]
    li_unique.append(numOfUnique)
    di_unique[key] = numOfUnique

# finding max num of unique digits
maxUnique = max(li_unique)

print("Key with most unique nums:", end = " ")

# output
for key in di_unique:
    if maxUnique == di_unique[key]:
        print(key, end=" ")

