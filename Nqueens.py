def is_safe(curr_row, curr_col, queens, columns, upper_left_diag, upper_right_diag):
    if columns[curr_col] == 0 and upper_right_diag[curr_col + curr_row] == 0 and upper_left_diag[curr_row - curr_col + queens - 1] == 0:
        return True
    return False

def set_1(curr_row, curr_col, queens, columns, upper_left_diag, upper_right_diag):
    columns[curr_col] = 1
    upper_left_diag[curr_row - curr_col + queens - 1] = 1
    upper_right_diag[curr_row + curr_col] = 1

def set_0(curr_row, curr_col, queens, columns, upper_left_diag, upper_right_diag):
    columns[curr_col] = 0
    upper_left_diag[curr_row - curr_col + queens - 1] = 0
    upper_right_diag[curr_row + curr_col] = 0

def place_n_queens(board, queens, curr_row, columns, upper_left_diag, upper_right_diag):
    if curr_row >= queens:
        return True

    for curr_col in range(queens):
        if is_safe(curr_row, curr_col, queens, columns, upper_left_diag, upper_right_diag):
            board[curr_row][curr_col] = 'Q'
            set_1(curr_row, curr_col, queens, columns, upper_left_diag, upper_right_diag)
            if place_n_queens(board, queens, curr_row + 1, columns, upper_left_diag, upper_right_diag):
                return True
            board[curr_row][curr_col] = '.'
            set_0(curr_row, curr_col, queens, columns, upper_left_diag, upper_right_diag)

    return False

if __name__ == "__main__":
    queens = int(input("Enter the number of queens: "))
    board = [['.'] * queens for _ in range(queens)]
    columns = [0] * queens
    upper_left_diag = [0] * (2 * queens - 1)
    upper_right_diag = [0] * (2 * queens - 1)

    place_n_queens(board, queens, 0, columns, upper_left_diag, upper_right_diag)

    for row in range(queens):
        for col in range(queens):
            print(board[row][col], end="  |  ")
        print()
