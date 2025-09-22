string = input("Enter the string: ")
result_str = string[0]
len_of_str = len(string)

for i in range(1, len_of_str):
    each_char = string[i]
    upper_case = each_char.upper()
    
    if each_char == upper_case:
        each_char = each_char.lower()
        result_str = result_str + "-" + each_char
    else:
        result_str = result_str + each_char
print(result_str) 
    
