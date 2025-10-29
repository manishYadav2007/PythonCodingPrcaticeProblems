
"""
    The function `get_indexes_of_subarray_sum` takes a list of integers and a target sum, and returns
    the indexes of the subarray that sums up to the target sum.
    
    :param arr: The `arr` parameter is a list of integers representing the input array. In this case,
    `arr = [1, 2, 3, 7, 5]`
    :param k: The `k` parameter in the `get_indexes_of_subarray_sum` function represents the target sum
    that you want to find in the subarray of the given array `arr`. In this case, `k` is set to 12, so
    the function is looking for a subarray within the
    :return: The function `get_indexes_of_subarray_sum` takes a list `arr` and a target sum `k` as input
    parameters. It finds the indexes of the subarray whose elements sum up to the target sum `k`.
    """

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
