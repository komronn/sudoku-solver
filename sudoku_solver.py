# Enable backtrack algorithm below to solve this board

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
]

def print_board(m):
    # if no board to print, print No Solution
    if m is None:
        print('No Solution')
        return
    line = '-'*25
    if m == []:
        print('Empty Matrix')
    num_of_rows = len(m)
    num_of_cols = len(m[0])

    for i in range(num_of_rows):
        # print line every 3 rows
        if i % 3 == 0:
            print(line)
        row_to_print = ''
        for j in range(num_of_cols):
            # print vertical bar every 3 column
            if j % 3 == 0:
                row_to_print += '| '
            value = str(m[i][j]) if m[i][j] > 0 else ' '
            row_to_print += value + ' '
        row_to_print += '|'
        print(row_to_print)
    print(line)

# checks if placing the value in [row,col] is valid in the board
def is_valid(board, row, col, value):
    # check the row for the same value
    for j in range(9):
        if board[row][j] == value:
            return False
    # check the grid for the same value
    grid_row = row // 3
    grid_col = col // 3
    for i in range(3):
        for j in range(3):
            if board[3*grid_row + i][3*grid_col + j] == value:
                return False
    return True

def find_zero(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j) # row, column  
    return None

def solve(board):
    cell = find_zero(board)
    if cell is None:
        return board
    row = cell[0]
    col = cell[1]
    # try numbers 1 to 9 on this cell
    for val in range(1,10):
        if (is_valid(board, row, col, val)):
            board[row][col] = val
            print_board(board)
            solution = solve(board)
            if solution is not None:
                return solution
                
            # this is a backtrack algorithm
            # board[row][col] = 0
    # if impossible to fill this cell, then return None
    return None

print_board(solve(board))