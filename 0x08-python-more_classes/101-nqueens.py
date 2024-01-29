#!/usr/bin/python3
"""N Queens problem."""


import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, n, solutions):
    """Solve N Queens problem using backtracking."""
    if row == n:
        solutions.append([i[:] for i in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n, solutions)
            board[row][col] = 0


def print_solutions(n, solutions):
    """Print the N Queens solutions."""
    for solution in solutions:
        print(solution)


def main():
    """Main function."""
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(n, solutions)


if __name__ == "__main__":
    main()
