



def get_string_rotation_count(str1, str2):
    if str1 == str2:
       return 0  
    
    rotated_string = str1

    for count in range(1, len(str1)):
        rotated_string = rotated_string[-1] + rotated_string[:-1]
    
        if rotated_string == str2:
            return count 
    return "No Match"


str1 = "python"
str2 = "onpyth"


result = get_string_rotation_count(str1, str2)
print(result)





