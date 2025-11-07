



arr = list(map(int, input("Enter the sequence of list items: ").split()))

result_arr  = []

len_of_arr  = len(arr) 


for i in range(len_of_arr):
    found_greater = False 
    
    for j in range(i + 1, len_of_arr):
        if arr[j] > arr[i]:
            result_arr.append(arr[j])
            found_greater = True 
            break 
    
    if not found_greater:
        result_arr.append(-1)

print(result_arr)




