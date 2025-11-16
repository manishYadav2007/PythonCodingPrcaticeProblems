







def get_sum_of_pairs(arr, k):
    stop_index = len(arr) 
    
    for cur_index in range(stop_index):
        num1 = arr[cur_index]
        num2 = k - num1 
        remaining_list  = arr[cur_index + 1:]
        
        if num2 in remaining_list:
            return True 
    else:
        return False 
            


arr  = list(map(int, input("Enter the list items: ").split()))
k = int(input("Enter the target value: "))
result = get_sum_of_pairs(arr,k)
print(result)
