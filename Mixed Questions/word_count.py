string = input("Enter the string value: ").lower().split() 
print(string)


dict = {}


for word in string:
    dict[word] = dict.get(word, 0) + 1 

sorted_words = sorted(dict.items()) 


for word, count in sorted_words:
    print(f"{word}: {count}")
 

