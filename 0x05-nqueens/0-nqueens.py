#!/usr/bin/python3
"""0-nqueens module."""

import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at position (row, col) on the board.
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """
    Utility function to solve the N queens problem recursively.
    """
    # If all queens are placed then add the solution
    if col == N:
        solutions.append([board[i][j] for i in range(N) for j in range(N)])
        return

    # Consider this column and try placing this queen in all rows
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, N, solutions)
            board[i][col] = 0


def solve_nqueens(N):
    """
    Solve the N queens problem and print all possible solutions.
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    for sol in solutions:
        print([[i, j] for i in range(N) for j in range(N) if sol[i*N+j] == 1])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solve_nqueens(sys.argv[1])
