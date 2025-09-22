

def count_elements_greater_than_previous_average(arr):
    running_sum = arr[0]
    prev_element_count = 1 
    result_count = 0 
    
    if len(arr) <= 1:
        return 0 
    
    len_of_arr  = len(arr) 
    for each_element in range(1, len_of_arr):
        
        current_element = arr[each_element]
        average = running_sum / prev_element_count 
        
        if current_element > average:
            result_count = result_count +  1 
            
        running_sum = running_sum +  current_element 
        prev_element_count = prev_element_count +  1 
    return result_count 







arr  = [100, 200, 150, 300]

result = count_elements_greater_than_previous_average(arr)

print(result)