n = int(input("Enter the value n: "))

list_of_n = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            list_of_n.append((i, j))
            
print(list_of_n)