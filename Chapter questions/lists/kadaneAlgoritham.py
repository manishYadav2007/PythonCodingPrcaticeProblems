import math 




def get_max_sum_subarray(arr):

    if not arr:
        return 0    
    max_num = math.inf 
    current_sum = 0 
    for each_num  in arr:
        current_sum += each_num 

        if current_sum > max_num:
            max_num = current_sum 
        
        
        if current_sum < 0:
            current_sum = 0 
    return max_num 






# arr = [2, 3, -8, 7, -1, 2, 3]
arr  = [-2, -4]

result = get_max_sum_subarray(arr)
print(result)



