




arr = [1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8 ,9, 9, 4, 2, 4, 5, 1]


count_element = {}

for i in arr:
    count_element[i] = count_element.get(i, 0) + 1 
print(count_element)

