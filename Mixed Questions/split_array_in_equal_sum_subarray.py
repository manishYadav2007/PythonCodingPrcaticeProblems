






def get_split_arr(arr):
    total_sum = sum(arr)
    
    if total_sum % 3 != 0:
        return "false" 
    
    target_sum = total_sum // 3
    current_sum = 0 
    parts_found = 0 
    
    for num  in arr:
        current_sum += num 
        if current_sum == target_sum:
            parts_found += 1 
            current_sum = 0 
    
    if parts_found >= 3:
        return "true"
    else:
        return "false"  



arr = [1, 3, 4, 0, 4]

result = get_split_arr(arr)
print(result)