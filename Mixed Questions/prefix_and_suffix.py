# str1 = input("Enter the string one: ")
# str2 = input("Enter the string two: ")

# result = ""

# for word in range(len(str1)):
#     if str2.startswith(str1[word:]):
#         result += str1[word:]
#         break
# else:
#     result = "No Overlapping" 

# print(result)








# string_one = input("Enter the string value one: ")
# string_two = input("Enter the string value two: ")


# result = ""




# for i in range(len(string_one)):
#     if string_two.startswith(string_one[i:]):
#         result += string_one[i:]
#         break
    
# else:
#     result = "No Overlapping"


# print(result)










str1 = input("Enter the string value one: ")
str2 = input("Enter the string value one: ")

result = ""

for i in range(len(str1)):
    if str2.startswith(str1[i:]):
        result += str1[i:]
        break 
else:
    result = "No Overlapping"

print(result)     
