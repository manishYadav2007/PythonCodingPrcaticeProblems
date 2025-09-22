

def get_k_sized_subarray_max(arr, k):
    s = []
    for end in range(1, len(arr)  + 1):
        for start in range(end):
            subarray = arr[start:end]
            s.append(subarray)  
    
    filter_arr  = []
    for j in s:
        if len(j) == k:
            filter_arr.append(max(j))
    return filter_arr 

arr  = [8, 5, 10, 7, 9, 4, 15, 12]
k = 4 
result = get_k_sized_subarray_max(arr, k) 
print(result)