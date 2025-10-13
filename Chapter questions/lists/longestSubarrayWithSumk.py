
# Approch 1

# arr = [10, 5, 2, 7, 1, -10]
# k = 15
# length_arr  = len(arr)
# subarray  = [arr[i:j+1] for i in range(length_arr) for j in range(i, length_arr)]

# max_len  = max((len(sub) for sub in subarray if sum(sub) == k), default=0)

# print(max_len)




# Approch 2


arr = [10, 5, 2, 7, 1, -10]
k = 15

len_arr  = len(arr)
prefSum = 0 
result = 0
hash_map = {}



for i in range(len_arr):
    prefSum += arr[i]


    if prefSum == k:
        result = i + 1 
    elif (prefSum - k) in hash_map:
        result = max(result, i - hash_map[prefSum  - k])
            
    
    if prefSum not in hash_map:
        hash_map[prefSum] = i

print(result)




















