



n = [1, 9, 2, 8, 6, 4, 3]
k = 100

subarray_elements = []

for end in range(1, len(n) + 1):
    for start in range(end):
        subarray = n[start:end]
        subarray_elements.append(subarray)
count = 0 
for each_array in subarray_elements:
    product = 1
    for each_element in each_array:
        product *= each_element 
    
    if product < k:
        count += 1 
print(count) 


    