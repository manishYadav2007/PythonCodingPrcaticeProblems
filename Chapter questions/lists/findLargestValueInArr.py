




def find_largest_value_in_arr(arr):

    if not arr:
        return None 

    max_value = arr[0]  
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value 


arr =  [5, 5, 5, 5]
result = find_largest_value_in_arr(arr)
print(result)