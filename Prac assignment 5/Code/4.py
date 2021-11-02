# form plaindromes from words entered

words = []
temp_word = ""
output_li_index = []
output_li_pal = []
j = 0

n = int(input("How many words: "))


# accept input
for i in range(n):
    word = input("Input: ")
    words.append(word)

for j in range (n):
    if j==0:
        for k in range (j+1,n):
            temp_word=words[j]+words[k]
            if temp_word == temp_word[::-1]:
                output_li_index.append("[",j,k,"]")
                output_li_pal.append(words[j]+words[k])
        
    else:
        for l in range (0,j):
            temp_word=words[j]+words[k]
            if temp_word == temp_word[::-1]:
                output_li_index.append("[",j,k,"]")
                output_li_pal.append(words[j]+words[k])

        for m in range (j+1,n):
            temp_word=words[j]+words[k]
            if temp_word == temp_word[::-1]:
                output_li_index.append("[",j,k,"]")
                output_li_pal.append(words[j]+words[k])
        

print("Output:",output_li_index)
print("The palindromes are",output_li_pal)