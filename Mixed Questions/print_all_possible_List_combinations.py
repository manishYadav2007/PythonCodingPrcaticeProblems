


n = list(map(int, input("Enter the list items: ").split()))



len_of_n = len(n)

for i in range(len_of_n):
    for j in range(len_of_n):
        for k in range(len_of_n):
            if i != j and j != k and i != k:
                print(n[i], n[j], n[k])
                
                
                
                