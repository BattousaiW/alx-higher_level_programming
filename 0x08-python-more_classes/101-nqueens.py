#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if a queen can be placed safely in this row
    for i in range(col):
        if board[row][i] == 1:
            return False
        if row - i >= 0 and board[row - i][col - i] == 1:
            return False
        if row + i < N and board[row + i][col - i] == 1:
            return False
    return True

def solve_n_queens_util(board, col):
    if col >= N:
        # All queens are placed, print the solution
        for row in range(N):
            print("".join("Q" if board[row][i] else "." for i in range(N)))
        print()
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens_util(board, col + 1):
                continue
            board[row][col] = 0

    return False

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens_util(board, 0):
        print("No solution exists.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4.")
            sys.exit(1)
        solve_n_queens(N)
    except ValueError:
        print("N must be a number.")
        sys.exit(1)
