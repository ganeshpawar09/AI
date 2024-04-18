def isSafe(board, n, currRow, currCol):
    # Check column
    for i in range(currRow):
        if board[i][currCol] == 'Q':
            return False

    # Check upper left diagonal
    row, col = currRow, currCol
    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col -= 1

    # Check upper right diagonal
    row, col = currRow, currCol
    while row >= 0 and col < n:
        if board[row][col] == 'Q':
            return False
        row -= 1
        col += 1

    return True


def solve(board, n, currRow):
    
    if currRow >= n:
        return True

    for currCol in range(n):
        if isSafe(board, n, currRow, currCol):
            board[currRow][currCol] = 'Q'
            if solve(board, n, currRow + 1):
                return True
            board[currRow][currCol] = '.'

    return False

if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    board = [['.'] * n for _ in range(n)]
    solve(board, n, 0)
    for currRow in range(n):
        for currCol in range(n):
            print(board[currRow][currCol], end=' |')
        print()
