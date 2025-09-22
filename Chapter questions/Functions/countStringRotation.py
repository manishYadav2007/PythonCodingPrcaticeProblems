





def get_str_rotation_count(str1, str2):
    
    
    if str1 == str2:
        return 0

    r = str1
    length_of_str = len(str1)
    
    for c in range(1, length_of_str):
        r =  r[-1] + r[:-1]
    
        if r  == str2:
            return c 
    return "No Match"                
    





str1 = input("Enter the First String: ").strip()
str2 = input("Enter the Second String: ").strip()
print(str1)
print(str2)
result = get_str_rotation_count(str1, str2)
print(result)
