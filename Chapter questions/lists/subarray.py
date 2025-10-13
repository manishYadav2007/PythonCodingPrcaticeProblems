




arr  =  [10, 5, 2, 7, 1, -10]


subarray_res = []




for end  in range(1, len(arr) + 1):
    for start in range(end):
        subarray_res.append(arr[start:end])
print(subarray_res)






