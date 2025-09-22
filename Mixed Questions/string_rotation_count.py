
def right_str_rotation(s):
    return s[-1] + s[:-1] 


def get_str_rotation_frequency(s1, s2):
    if (s1 == s2):
        return 0 
    
    rotated_str = s1 
    for count in range(1, len(s1)):
        rotated_str = right_str_rotation(rotated_str) 
    
        if rotated_str == s2:
            return count 
    return "No Match"






s1 = input().strip() 
s2 = input().strip() 
result = get_str_rotation_frequency(s1, s2)
print(result) 

