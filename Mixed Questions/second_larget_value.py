

def get_second_largest_value(arr):
    unique_element = set(arr) 
    if len(unique_element) > 1:
        list_object = list(unique_element)
        list_object.sort() 
        return list_object[-2] 
    else:
        return -1  




arr  = [28004, 23544, 32504, 29493, 17013, 17850, 18952, 12089, 5126, 10353]

result = get_second_largest_value(arr) 
print(result) 