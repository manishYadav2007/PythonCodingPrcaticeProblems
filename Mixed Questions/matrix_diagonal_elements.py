# def get_diagonal_matrix(matrix, n, m):
#     diagonal_row = []
#     for row in range(n):
#         if row < m:
#             diagonal_row.append(matrix[row][row])
#     return diagonal_row

# n, m = list(map(int, input("Enter the matrix order: ").split()))
# matrix = [list(map(int, input("Enter the matrix input: ").split())) for i in range(n)]
# diagonal_elements = get_diagonal_matrix(matrix, n, m)
# print(diagonal_elements)




def get_diagonal_matrix(matrix, row, column):
    diagonal_matrix = []
    
    
    for each_row in range(row):
        if each_row < column:
            diagonal_matrix.append(matrix[each_row][each_row])
    return diagonal_matrix 

        


row, column = list(map(int, input("Enter the order of matrix: ").split()))

matrix = [list(map(int, input("Enter the matrix rows: ").split())) for _ in range(row)]
print(matrix)


result = get_diagonal_matrix(matrix, row, column)
print(result)
