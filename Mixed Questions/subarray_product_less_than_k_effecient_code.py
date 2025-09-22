n = [1, 2, 3, 4]
k = 10


if k <= 1:
    count = 0 
else:
    count = 0 
    product = 1 
    start = 0 
    for end in range(len(n)):
        product *= n[end] 
        
        while product >= k:
            product //= n[start]
            start += 1 
        
        
        count += (end - start + 1)
print(count)
        



