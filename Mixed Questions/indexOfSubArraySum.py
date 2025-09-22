




# def find_sub_array_sum(userArrayInput, k):
#     length = len(userArrayInput)
#     start_pointer = 0 
#     current_sum = 0 
    
#     for end_point in range(length):
#         current_sum = current_sum + userArrayInput[end_point] 
    
#         while current_sum > k and start_pointer <= end_point:
#             current_sum -= userArrayInput[start_pointer]
#             start_pointer += 1 
    
#         if current_sum == k:
#             return [start_pointer + 1, end_point + 1] 

#     return [-1]
    
    
    



# userArrayInput  = list(map(int, input("Enter the list items: ").split()))
# k = int(input("Enter the target value: "))


# result = find_sub_array_sum(userArrayInput, k) 
# print(result)







def find_sub_array_sum(arr, target_sum):
    """
    The function `find_sub_array_sum` takes a list of integers and a target sum, and returns the indices
    of the subarray that sums up to the target sum.
    
    :param arr: The `arr` parameter in the `find_sub_array_sum` function is a list of integers. This
    function aims to find a subarray within the given list `arr` that sums up to the `target_sum`
    provided as another parameter. If such a subarray is found, the function returns
    :param target_sum: The `find_sub_array_sum` function takes in two parameters:
    :return: The function `find_sub_array_sum` returns a list containing the indices of the subarray
    whose sum is equal to the target sum. If no such subarray is found, it returns -1.
    """
    
    
    len_of_list = len(arr)
    start  = 0 
    current_sum = 0 
    
    for end in range(len_of_list):
        current_sum += arr[end]
        
        while current_sum > target_sum and start <= end:
            current_sum -= arr[start]
            start += 1 
        
        if current_sum == target_sum:
            return [start + 1, end + 1]
    return -1 






arr  = list(map(int, input("Enter the list items: ").split()))
target_sum = int(input("Enter the target value: "))

result = find_sub_array_sum(arr, target_sum)
print(result)