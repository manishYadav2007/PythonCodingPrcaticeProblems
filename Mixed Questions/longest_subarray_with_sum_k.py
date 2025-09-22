




def get_longest_subarray(arr, k):
    psm = {0: -1}
    
    cs = 0 
    ml = 0 
    
    for i, num in enumerate(arr):
        cs += num 
        
        if (cs - k) in psm:
            l = i - psm[cs - k]
            ml = max(ml,  l) 
        
        
        if cs not in psm:
            psm[cs] = i 
    return ml 
            



arr  = [-5, 8, -14, 2, 4, 12] 
k = -5 

result = get_longest_subarray(arr, k)
print(result) 
