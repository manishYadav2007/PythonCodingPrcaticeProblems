# m, n = list(map(int, input("Entr the m and n: ").split()))

# matrix = [list(map(int, input("Enter the matrix: ").split())) for _ in range(m)]

# combine_matrix = []


# for row in matrix:
#     for numbers in row:
#         combine_matrix.append(numbers)
# print(combine_matrix)

# combine_matrix.sort()



# index = 0


# for _ in range(m):
#     row_numbers =  combine_matrix[index:index + n]
#     print(" ".join(map(str, row_numbers)))
#     index += n 











m, n = list(map(int, input("Enter the order of matrix: ").split())) 
matrix = [list(map(int, input("Enter the matrix input: ").split())) for _ in range(1, m + 1 )]




new_matrix = []

for each_list in matrix:
    for each_row in each_list:
        new_matrix.append(each_row)

new_matrix.sort(); 


index = 0

for i in range(m):
    row_num = new_matrix[i:i+n]
    print(" ".join(map(str, row_num)))
    index += n 
    
























