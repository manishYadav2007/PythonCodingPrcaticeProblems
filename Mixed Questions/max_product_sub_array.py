

def  product_array_puzzle(array):
    length = len(array)
    result_array = [1] * length 
    for i in range(length):
        for j in range(length):
            if i != j:
                result_array[i] *= array[j]
    return result_array
        



array =[12, 0]
result = product_array_puzzle(array)
print(result)
