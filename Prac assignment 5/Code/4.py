# form plaindromes from words entered

n = int(input("Number of words to be entered: ")) 
input_list = [] 
output_index = []
output_palin = []

for i in range (n): 
          word = input("Enter the word: ") 
          input_list.append(word) 

for j in range (len(input_list)): 
    for k in range (len(input_list)): 
        if (k!=j): 
            new_word = input_list[j]+input_list[k] 
            if (new_word == new_word[::-1]): 
                new_word_list = [j,k] 
                output_index.append(new_word_list) 
                output_palin.append(new_word) 

print("Output:",output_index)
print("Explanation: The panidromes are",output_palin)

