



def find_floor_sorted_array(arr, x):
    
    result_index = -1 

    for i in range(len(arr)):
        if arr[i] <= x:
            result_index = i 
        else:
            break 
    return result_index 




arr =  [1, 2, 8, 10, 10, 12, 19]
x = 11
result = find_floor_sorted_array(arr, x)
print(result)