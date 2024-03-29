#!/usr/bin/python3
import sys
from itertools import permutations


def is_valid(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) == abs(board[i] - board[j]):
                return False
    return True


def solve_n_queens(n):
    solutions = []
    for perm in permutations(range(n)):
        board = list(perm)
        if is_valid(board):
            solutions.append(board)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    solutions = solve_n_queens(n)
    for sol in solutions:
        board = [[" " for _ in range(n)] for _ in range(n)]
        for i, j in enumerate(sol):
            board[i][j] = "Q"
        print(board)
