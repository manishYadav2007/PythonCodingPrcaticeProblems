


def find_peak_element(arr):
    length = len(arr)

    if length == 1:
        return 0 
    
  # The code `if arr[0] > arr[1]: return 0` is checking if the first element in the array `arr` is
  # greater than the second element. If this condition is true, it means that the first element is a
  # peak element in the array because it is greater than its immediate neighbor to the right. In this
  # case, the function returns 0 as the index of the peak element.
    if arr[0] > arr[1]:
        return 0 
    
# The code `if arr[length - 1] > arr[length - 2]: return length - 1` is checking if the last element
# in the array `arr` is greater than its immediate neighbor to the left. If this condition is true, it
# means that the last element is a peak element in the array because it is greater than its immediate
# neighbor to the left. In this case, the function returns the index of the last element as the peak
# element.
    if arr[length - 1] > arr[length - 2]:
        return length - 1
    
# This part of the code is implementing a loop that iterates over the elements of the input array
# `arr` starting from the second element (index 1) up to the second-to-last element (index `length -
# 2`).
    for i in range(1, length - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return i 
    return -1




    




arr =  [1, 2, 4, 5, 7, 8, 3]


result = find_peak_element(arr)
print(result)