

def get_unique_occurance_of_digits(n, arr):
    occurance_result = []
    processed_number = []
    for i in arr:
        if i not in processed_number:
            count_digit = arr.count(i)
            occurance_result.append(count_digit)
            
            processed_number.append(i)
    return len(occurance_result) == len(set(occurance_result))
                 




n = 5
# arr  = [2, 2, 5, 10, 1, 2, 10, 5, 10, 2]
# arr = [1, 1, 2, 5, 5]
arr = [5, 5, 1, 7, 8, 8, 9, 5]

result = get_unique_occurance_of_digits(n, arr)
print(result)


 

