




def find_rotation_of_array(arr, d):
    n = len(arr)

    f = d % n 
    
    first_part = arr[:f]
    print(first_part)
    second_part = arr[f:]
    rotated_list = second_part + first_part 
    return rotated_list 
arr = [7, 3, 9, 1]
d = 9
result = find_rotation_of_array(arr, d)
print(result)

