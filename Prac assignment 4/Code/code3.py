# check palindromes
st = input("Enter a string: ")
temp = ""
count = 0
st_split = st.split(" ")

for word in st_split:
    if word == word[::-1] and word.isalnum():
        print(st.find(" " + word) + 1, word)
    
