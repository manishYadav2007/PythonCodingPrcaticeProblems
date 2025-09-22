



def tic_tae_toe(board):
    
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    for col in range(3):
        
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    
    
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] == board[0][1] == board[0][0]:
        return board[0][2] 
    
    






row_one = input("Enter the first row: ").split()
row_two = input("Enter the second row: ").split()
row_three = input("Enter the third row: ").split()



board = [row_one, row_two, row_three]

result = tic_tae_toe(board) 

winner = result.lower() 


if winner == "o":
    print("Abhinav Wins")
elif winner == "x":
    print("Anjali Wins")
else:
    print("Tie") 

