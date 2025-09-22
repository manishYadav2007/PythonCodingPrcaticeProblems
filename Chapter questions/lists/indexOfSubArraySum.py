

def  get_indexes_of_subarray_sum(arr, k):
    current_sum = 0 
    start_pointer = 0 
    len_of_list = len(arr)
    
    for end_pointer in range(len_of_list):
        current_sum += arr[end_pointer]
        
        
        
        while current_sum > k and start_pointer <= end_pointer:
            current_sum -= arr[start_pointer]
            start_pointer += 1 
        
        
        if current_sum == k:
            return [start_pointer + 1, end_pointer + 1]
    return [-1]





arr  = [1, 2, 3, 7, 5]
k = 12

result = get_indexes_of_subarray_sum(arr, k)
print(result)
