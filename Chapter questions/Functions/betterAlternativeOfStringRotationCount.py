



def solve_with_concatenation(str1, str2):
    
    if len(str1) != len(str2) or not str1:
        return "No Match" if str1 != str2 else 0


    if str1 == str2:
        return 0 
    
    temp_str = str1 + str1 

    rotations = temp_str.find(str2)
    
    return rotations if rotations != -1 else "No Match" 


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

result = solve_with_concatenation(str1, str2)
print(result)