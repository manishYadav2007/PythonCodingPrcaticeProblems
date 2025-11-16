


def find_min_heights(arr, k):
    n = len(arr) - 1
    
    if n <= 1:
        return 0

    arr.sort()
    # print(arr)
    min_diff = arr[n] - arr[0]
    # return min_diff 
    
    for each_tower in range(1, n):

        if arr[each_tower] - k < 0:
            continue

        temp_min = min(arr[0] + k, arr[each_tower] - k)
        temp_max = max(arr[each_tower - 1] + k, arr[n] - k)
        min_diff =  min(min_diff, temp_max - temp_min)

    return min_diff




    
# arr = [2, 4, 3, 9, 9, 10, 9, 7, 1, 2]
# k = 4


arr = [3, 9, 12, 16, 20]
k = 3
result = find_min_heights(arr, k)
print(result)
