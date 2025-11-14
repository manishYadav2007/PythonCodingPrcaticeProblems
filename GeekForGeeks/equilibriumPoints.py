





def findEquilibriumPoint(arr):
    total_sum = sum(arr)
    left_sum =  0
    for j in range(len(arr)):
        cur_num = arr[j]
        right_sum = total_sum - left_sum - cur_num 

        if left_sum == right_sum:
            return j 

        left_sum += cur_num 
    return -1




arr =  [1, 2, 3]

result = findEquilibriumPoint(arr)
print(result)