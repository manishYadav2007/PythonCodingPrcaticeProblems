




def get_longest_subarray(arr, k):
    length_result = {}
    for i in range(len(arr)):
        temp_sum = 0
        for j in range(i, len(arr)):
            temp_sum += arr[j]
            
            if temp_sum == k:
                length_result[j-i+1] = arr[i:j+1]








arr  = [10, -10, 20, 30]
k = 5

result = get_longest_subarray(arr, k)
print(result)