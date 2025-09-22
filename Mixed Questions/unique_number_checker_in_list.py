def check_unique_num(list):
    
    if len(list) == len(set(list)):
        return True 
    else:
        return False





list  = [1, 2,  3, 7, 9]
result = check_unique_num(list)
print(result)

