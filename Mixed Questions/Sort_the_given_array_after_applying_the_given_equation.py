


def get_array_equation(arr,a, b, c):
    return sorted([a * (x * x) + b  * x + c for x in arr])





arr = [-3, -1, 2, 4]
a = -1
b = 0
c = 0 

result = get_array_equation(arr, a, b, c)
print(result)