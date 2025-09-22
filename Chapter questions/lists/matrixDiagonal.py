



def get_diagonal_matrix(matrix, row, column):
    diagonal_matrix = []
    
    for each_row in range(row):
        if each_row < column:
            diagonal_matrix.append(matrix[each_row][each_row])
    return diagonal_matrix  





row, column = list(map(int, input("Enter the order of the matrix: ").split()))

matrix = [list(map(int, input("Enter the matrix input: ").split())) for _ in range(row)]


result = get_diagonal_matrix(matrix, row, column)
print(result)


