# n = int(input("Enter the matrix size: " ))

# matrix = [list(map(int, input("Enter the matrix: ").split())) for _ in range(n)]

# anti_diagonal = []



# # for row in matrix:
# #     print(row)

# for i in range(n):
#     anti_diagonal.append(matrix[i][n - 1 - i])
# print(anti_diagonal)


    


n = int(input("Enter the order of matrix: "))
matrix = [list(map(int, input("Enter the matrix input: " ).split())) for _ in range(n)]
anti_diagonal = [matrix[i][n - 1 - i] for i in range(n)]
print(anti_diagonal)




