
"""
    The function `longest_subarray_with_0_sum` finds the length of the longest subarray with a sum of 0
    in a given array.
    
    :param arr: The `arr` parameter in the `longest_subarray_with_0_sum` function is a list of integers.
    In this case, the `arr` list is `[15, -2, 2, -8, 1, 7, 10, 23]`. The
    :return: The function `longest_subarray_with_0_sum` is being called with the array `arr = [15, -2,
    2, -8, 1, 7, 10, 23]`. The function calculates the length of the longest subarray with a sum of 0
    within the given array.
    """




def longest_subarray_with_0_sum(arr):
    first_index = {0: -1}
    prefix = 0 
    max_len = 0 

    for i, val in enumerate(arr):
        # print(f"Index: {i} Value: {val}")
        prefix += val 

        if prefix not in first_index:
            first_index[prefix] = i 
        else:
            length = i - first_index[prefix]
        
            if length > max_len:
                max_len = length 
    return max_len 

arr =  [15, -2, 2, -8, 1, 7, 10, 23]

# longest_subarray_with_0_sum(arr)

result  = longest_subarray_with_0_sum(arr)
print(result)