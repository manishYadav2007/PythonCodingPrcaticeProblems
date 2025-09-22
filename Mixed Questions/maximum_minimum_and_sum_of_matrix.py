




def get_sum_max_and_min(combine_matrix):
    return max(combine_matrix), min(combine_matrix), sum(combine_matrix)



n, m  =  list(map(int, input("Enter the matrix order: ").split()))

matrix = []

for row in range(1, n + 1):
    matrix_input = list(map(int, input("Enter the matrix input: ").split()))
    matrix.append(matrix_input)



combine_matrix  = []

for row in matrix:
    for i in row:
        combine_matrix.append(i)


result = get_sum_max_and_min(combine_matrix)


for result_element in result:
    print(result_element)
   


