




arr  = [1, 3, 2, 4]
result = []
len_of_arr  = len(arr) 

for i in range(len_of_arr):
    if arr[i:] > arr[i + 1]:
        result.append(i)
    else:
        result.append(-1)
print(result)


        





