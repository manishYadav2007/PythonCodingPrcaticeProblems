string = input("Enter the string: ")

len_of_str = len(string)

result_str = string[0]

for i in range(1, len_of_str):
    each_char = string[i]
    upper_case = each_char.upper()
    
    if each_char == upper_case:
        result_str = result_str +  " " + each_char
    else:
        result_str = result_str +  each_char
print(result_str)




