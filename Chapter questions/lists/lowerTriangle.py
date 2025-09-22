








rows, column = list(map(int, input("Enter the order of matrix: ").split()))

matrix = [list(map(int, input("Enter the matrix input: ").split())) for _ in range(rows)]



"""
[
[1, 2, 3],
[10, 20, 30],
[5, 10, 15]
]



rows = 3 
col = 3 


"""



for each_row in range(len(matrix)):
    num_list  = matrix[each_row][:each_row + 1]
    print(num_list)
    
        



