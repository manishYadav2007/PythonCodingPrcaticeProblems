

def find_duplicates(arr):
    s = set()
    
    duplicate = []
    for n in arr:
        if n in s:
            duplicate.append(n) 
        else:
            s.add(n)  
    return duplicate 


arr  = [3, 1, 2, 1, 2, 4, 5, 7]

result = find_duplicates(arr)
print(result)






