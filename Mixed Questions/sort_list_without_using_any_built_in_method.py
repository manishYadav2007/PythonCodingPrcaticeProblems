






def  sort_list(arr):
    
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    return arr




arr = [7, 10, 4, 3, 20, 15]

result = sort_list(arr)

print(result)