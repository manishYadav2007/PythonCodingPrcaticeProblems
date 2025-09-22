
def  get_matrix_sum(first_matrix, second_matrix, n, m):
    matrix_sum_result = []
    for row in range(n):
        row_result = []
        for col in range(m):
            sum_of_matrix = first_matrix[row][col] + second_matrix[row][col]
            row_result.append(sum_of_matrix)
        matrix_sum_result.append(row_result)
    return matrix_sum_result


n, m = list(map(int, input("Enter the matrix order: ").split()))

first_matrix = [list(map(int, input("Enter the first matrix digits: ").split())) for i in range(n)]


second_matrix = [list(map(int, input("Enter the second matrix digits: ").split())) for i in range(n)]


matrix_sum = get_matrix_sum(first_matrix, second_matrix, n, m)

for each_row in matrix_sum:
    print(each_row)
