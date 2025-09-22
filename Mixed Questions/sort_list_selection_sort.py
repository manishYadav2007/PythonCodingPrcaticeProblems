


def sort_list(my_list):
    n = len(my_list)
    
    for i in range(n): 
        min_index = i 
        
        for j in range(i + 1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j 
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i] 
    return my_list 





my_list = [64, 34, 25, 12, 22, 11, 90]

result = sort_list(my_list)
print(result)