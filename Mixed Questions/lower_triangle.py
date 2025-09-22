def  get_triangle_matrix(matrix):    
    for each_row in range(len(matrix)):
        triangle_matrix   = matrix[each_row][:each_row + 1]
        print(triangle_matrix)    



n, m = list(map(int, input("Enter the order of matrix: ").split()))
matrix = [list(map(int, input("Enter the matrix input: " ).split())) for i in range(n)]
get_triangle_matrix(matrix)


