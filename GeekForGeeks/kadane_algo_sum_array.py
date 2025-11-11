import math 

def get_sum_of_array(array):
    if not array:
        return 0 
    
    max_so_far = -math.inf 
    current_sum = 0 
    
    for num in array:
        current_sum += num 
        if current_sum > max_so_far:
            max_so_far = current_sum 
        
        if current_sum < 0:
            current_sum = 0 
    return max_so_far 




# array  = [5, 4, 1, 7, 8]
array  = [2, 3, -8, 7, -1, 2, 3]
result = get_sum_of_array(array)
print(result)

