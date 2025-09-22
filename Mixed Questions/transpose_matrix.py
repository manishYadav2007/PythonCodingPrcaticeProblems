

# def get_transpose(matrix_row, n, m):
#     transpose = []
#     for row in range(n):
#         row_result = []
#         for col in range(m):
#             row_result.append(matrix_row[col][row])
#         transpose.append(row_result)

# n, m = list(map(int, input("Enter the order of matrix: ").split()))
# matrix_row = [list(map(int, input("Enter the matrix: ").split())) for i in range(1, n + 1)]
# transpose_result = get_transpose(matrix_row, n, m)
# for each_row in transpose_result:
#     print(each_row)
    
    
    



def  get_transpose(matrix, m, n):
    transpose_matrix = [] #  Initialize an empty list to store the transpose matrix
    for i in range(n): #  Iterate through columns of original matrix (rows of transpose)
        row = []
        for j in range(m): #  Iterate through rows of original matrix (columns of transpose)
            row.append(matrix[j][i]) #  Append element at position (j,i) to the new row
        transpose_matrix.append(row) #  Add the new row to the transpose matrix
    return transpose_matrix #  Return the computed transpose matrix
        


m, n  = list(map(int, input("Enter the order of matrix: ").split())) #  Read the dimensions of the matrix (m rows and n columns)


matrix = [list(map(int, input("Enter the matrix values: ").split())) for _ in range(m)] #  Read the matrix elements row by row


result = get_transpose(matrix, m, n) #  Compute the transpose of the matrix


for i in result: #  Print each row of the transpose matrix
    print(i)
    

