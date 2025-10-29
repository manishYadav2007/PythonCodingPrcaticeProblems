



"""
    The function `count_inversion_array` calculates the number of inversions in an array.
    
    :param arr: The `arr` parameter in the `count_inversion_array` function is a list of integers
    representing an array. In this case, the array `arr` is `[2, 4, 1, 3, 5, 7, 1]`. The function
    calculates the number
    :return: The function `count_inversion_array` is returning the count of inversions in the input
    array `arr`.
    """
def count_inversion_array(arr):
    count_inversion  = 0 
    len_of_arr  = len(arr)
    for i in range(len_of_arr + 1):
        for j in range(i + 1, len_of_arr):
            if i < j and arr[i] > arr[j]:
                count_inversion += 1 
    return count_inversion       

arr  = [2, 4, 1, 3, 5, 7, 1]

result = count_inversion_array(arr)
print(result)






print(" Hello World ")







