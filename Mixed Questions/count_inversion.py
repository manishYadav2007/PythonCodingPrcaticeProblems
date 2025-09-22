


def get_count_inversion(list_num):
    n = len(list_num) 
    inversion_count = 0 
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if list_num[i] > list_num[j]:
                inversion_count += 1 
    return inversion_count 
    





list_num =  [95, 13, 47, 52, 41, 68, 42]
result = get_count_inversion(list_num)
print(result)

