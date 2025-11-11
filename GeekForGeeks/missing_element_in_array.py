


# def get_missing_element(arr):
#     length = len(arr) + 1
#     sum_of_target_range = length * (length + 1 ) / 2 
#     sum_of_arr  = sum(arr) 
#     diff = int(sum_of_target_range - sum_of_arr)
#     return  diff 


# arr  = [8, 2, 4, 5, 3, 7, 1]
# result = get_missing_element(arr)
# print(result) 






def missingNumber(arr):
    n = len(arr) + 1 
    expected_sum = n * (n + 1) / 2 
    print(expected_sum)
    return int(expected_sum - sum(arr)) 
    

arr =[1, 2, 3, 5]
result = missingNumber(arr)
print(result)  

