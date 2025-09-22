

def find_number_of_occurance(arr, k):
    # count_num = arr.count(k)
    # return count_num 
    count_num = 0 
    
    for i in range(len(arr)):
        if arr[i] == k:
            count_num += 1 
    return count_num 


arr  =[1, 1, 2, 2, 2, 2, 3]
k = 4 

result = find_number_of_occurance(arr, k)
print(result)