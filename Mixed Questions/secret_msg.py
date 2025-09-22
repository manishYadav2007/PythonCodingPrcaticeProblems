# string = input("Enter the string: ").lower()

# words = string.split()


# result = []

# for char  in string:
#     encoded_string = []
#     for word in char:
#         if word.isalpha():
#             position = ord(word) - ord("a") + 1
#             encoded_string.append(str(position))
#     result.append("-".join(encoded_string))
    
    
#     final_result = " ".join(result)
    
# print(final_result)

            
            
            

string_value = input("Enter the string value: ")

result = ""



for each_char in string_value:
    if each_char.isalpha:
        lower_case = each_char.lower()
        mirror_str = chr(219 - ord(lower_case))
        result += mirror_str 
    else:
        result += each_char 

print(result)





        




