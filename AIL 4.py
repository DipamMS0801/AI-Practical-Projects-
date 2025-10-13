def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] else ".", end=" ")
        print()
    print()


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j]:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queen(board, row, n):
    # Base case: All queens placed
    if row == n:
        print_solution(board, n)
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            res = solve_n_queen(board, row + 1, n) or res
            board[row][col] = False  # Backtrack
    return res


def n_queen(n):
    board = [[False for _ in range(n)] for _ in range(n)]
    if not solve_n_queen(board, 0, n):
        print("No solution exists")


# Example: Change n for different board sizes
n = int(input("Enter the number of queens: "))
n_queen(n)
