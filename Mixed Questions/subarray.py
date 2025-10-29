# numbers = list(map(int, input("Enter the list elements: " ).split()))


numbers = [5, 2, 3, 10, 6, 8]
k = 10 

subarray_elements = []


for end  in range(1, len(numbers) + 1):
    for start in range(end):
        subarray = numbers[start:end]
        subarray_elements.append(subarray)

count = 0 

for subarray_items in subarray_elements:
    if sum(subarray_items) == k:
        count += 1 
 
print(count)

 

    