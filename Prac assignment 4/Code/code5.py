# check if str2 is in the end of str1
str1 = input("Enter string: ")
str2 = input("Enter string: ")

if str2.lower().endswith(str1.lower()) or str1.lower().endswith(str2.lower()):
    print("True")
else:
    print("False")

    