


def get_majority_element(arr):
    n = len(arr) / 2 
    m = {}
    for i in arr:
        m[i] = m.get(i, 0) + 1 
    
    for key, value in m.items():
        if value > n:
            return key 
    return -1

# arr  = [1, 1, 2, 1, 3, 5, 1]
arr  = [2, 13]

result = get_majority_element(arr)
print(result)

