from functools import reduce 

def get_traverse_arr(arr):
    return  reduce(lambda s1, s2 : f"{s1} {s2}", arr)



list_num = [41, 45, 85, 37]

result = get_traverse_arr(list_num)
print(result)
print(len(result))





