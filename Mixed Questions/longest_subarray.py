




arr =  [10, 5, 2, 7, 1, -10]
k = 15


# subarray_result = []
length = []

    
for i in range(len(arr)):
    temp_sum =  0;
    for j in range(i, len(arr)):
        temp_sum += arr[j]
        
        if temp_sum == k:
            length.append(j - i + 1)
        else:
            length.append(0)
print(max(length))       





    
    
    
    
    
    
    
    
    
    
    
    
    
    
