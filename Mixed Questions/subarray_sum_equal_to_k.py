



arr  = [1, 2, 3, 7, 5]
k = 12

subarray = []
sum_of_subarray = 0 


for end in range(1, len(arr) + 1):
    for start in range(end):
        subarray_el = arr[start:end]
        subarray.append(subarray_el)
        print(subarray) 
        
        
