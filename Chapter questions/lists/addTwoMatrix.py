


def get_sum_of_matrix(matrix1, matrix2, row, column):
    sum_matrix = []
    
    for row in range(row):
        row_sum_result = []
        for col in range(column):
            value = matrix1[row][col] + matrix2[row][col]
            row_sum_result.append(value)
        sum_matrix.append(row_sum_result)
    return sum_matrix 



row, column = list(map(int, input("Enter the order of matrix: ").split()))


matrix1 = [list(map(int, input("Enter the matrix one input: ").split())) for _ in range(row)]
matrix2 = [list(map(int, input("Enter the matrix two input: ").split())) for _ in range(row)]



result = get_sum_of_matrix(matrix1, matrix2, row, column)



for each_row in result:
    print(each_row)
    

