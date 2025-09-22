
def  add_matrix(matrix_one, matrix_two, row, column):
    matrix_result = []
    for each_row in range(row):
        row_result  = []
        for each_column in range(column):
            sum_of_matrix = matrix_one[each_row][each_column] + matrix_two[each_row][each_column]
            row_result.append(sum_of_matrix)
        matrix_result.append(row_result)
    return matrix_result 
    

row, column = list(map(int, input("Enter the order of matrix: ").split()))

matrix_one = [list(map(int, input("Enter the value of matrix one: ").split())) for _ in range(row)]
matrix_two = [list(map(int, input("Enter the value of matrix one: ").split())) for _ in range(row)]

result = add_matrix(matrix_one, matrix_two, row, column)
print(result)

for each_row in result:
    print(each_row)
    

