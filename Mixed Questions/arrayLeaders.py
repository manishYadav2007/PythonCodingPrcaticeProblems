



def get_arr_leaders(arr):
    leaders = []
    if not arr:
        return []
    
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)
    
    return leaders[::-1] 





arr  =[30, 10, 10, 5]
result = get_arr_leaders(arr)
print(result)