from functools import reduce 


def get_common_elements_in_sets( matrix):    
    common_elements = reduce(lambda s1, s2: s1 & s2, matrix)
    return common_elements

num_of_rows = int(input("Enter the number of rows: "))
matrix = [set(map(int, input("Enter the list items: ").split()))  for _ in range(num_of_rows)]
result = get_common_elements_in_sets(matrix)
result = sorted(result) 
print(result) 

