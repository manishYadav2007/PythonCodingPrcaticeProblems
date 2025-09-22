


def get_list_item(arr, k):
    return "".join(str(i) for i in arr if i < k)




arr = [54, 43, 2, 1, 5]
k = 6 
result = get_list_item(arr, k)
print(result)


