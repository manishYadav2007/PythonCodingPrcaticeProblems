


def find_peak_element(arr):
    length = len(arr)

    if length == 1:
        return 0 
    
    if arr[0] > arr[1]:
        return 0 
    

    if arr[length - 1] > arr[length - 2]:
        return length - 1
    

    for i in range(1, length - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return i 
    return -1




    




arr =  [1, 2, 4, 5, 7, 8, 3]


result = find_peak_element(arr)
print(result)