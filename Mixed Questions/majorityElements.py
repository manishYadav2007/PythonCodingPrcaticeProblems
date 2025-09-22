


def get_majority_element(arr):
    
    m = len(arr) / 3 
    c = {}
    for i in arr:
        c[i] = c.get(i, 0) + 1 
        
    result = []
    for k, v in c.items():
        if v > m:
            result.append(k)
    return sorted(result)


arr  =  [3, 2, 2, 4, 1, 4]

result = get_majority_element(arr)
print(result)
