




arr  =  [1, 2, 3, 7, 5]


subarray_res = []




for end  in range(1, len(arr) + 1):
    for start in range(end):
        subarray_res.append(arr[start:end])
print(subarray_res)








