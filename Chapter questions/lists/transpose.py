



def get_transpose(matrix, row, column):
    """
     [
       [ 1, 2, 3],
        [10, 20, 30],
        [5, 10, 15]    
    ] """
    
    
    """
        row = 3 
        column = 3
    """
    
    
    transpose_matirx = []
    for each_col in range(column):
        rows = []
        for each_row in range(row):
            rows.append(matrix[each_row][each_col])
        transpose_matirx.append(rows)
    return transpose_matirx 





row, column  = list(map(int, input("Enter the order of the matrix: ").split()))
print((row, column))
matrix = [list(map(int, input("Enter the matrix input: ").split())) for _ in range(row)]



result = get_transpose(matrix, row, column)



for each_row in result:
    print(each_row)