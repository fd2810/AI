def print_board(board, n):
    print("\nSolution:\n")
    print("+" + "---+" * n)
    for row in board:
        print("|" + "|".join(" Q " if col else "   " for col in row) + "|")
        print("+" + "---+" * n)
    print("\n" + "=" * (4 * n))  # separator between solutions

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    return True

def solve_nqueens(board, row, n):
    if row == n:
        print_board(board, n)
        return True
    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            res = solve_nqueens(board, row + 1, n) or res
            board[row][col] = False
    return res

def nqueens(n):
    board = [[False] * n for _ in range(n)]
    if not solve_nqueens(board, 0, n):
        print("No solution exists")

if __name__ == "__main__":
    n = int(input("Enter the number of queens (N): "))
    nqueens(n)
 
