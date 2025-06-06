def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, row, n):
    if row == n:
        for r in board:
            print(r)
        print()
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n)
            board[row][col] = 0  # backtrack

n = 4
board = [[0]*n for _ in range(n)]
solve(board, 0, n)
