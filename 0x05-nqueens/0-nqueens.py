#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col]
    # in the current configuration of the board.
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve_nqueens(N):
    # Initialize the chessboard with all zeros.
    board = [-1] * N
    solutions = []

    def backtrack(col):
        if col == N:
            # If all queens are placed successfully, add the solution to the list.
            solutions.append([[i, board[i]] for i in range(N)])
            return

        for i in range(N):
            if is_safe(board, i, col, N):
                board[col] = i
                backtrack(col + 1)
                board[col] = -1

    backtrack(0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        print(solution)
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
