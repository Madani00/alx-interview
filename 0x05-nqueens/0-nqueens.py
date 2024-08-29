#!/usr/bin/python3
"""python algorithm"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

col = set()
positiveD = set()
negativeD = set()

res = []
board = [[""] * n for _ in range(n)]


def backtrack(r, n, res, board, col, positiveD, negativeD):
    """ N-queens """
    if r == n:
        sol = ["".join(map(str, row)) for row in board]
        res.append([[i, int(sol[i])] for i in range(n)])
        return

    for c in range(n):
        if c in col or (r+c) in positiveD or (r-c) in negativeD:
            continue
        col.add(c)
        positiveD.add(r+c)
        negativeD.add(r-c)
        board[r][c] = c

        backtrack(r+1, n, res, board, col, positiveD, negativeD)
        col.remove(c)
        positiveD.remove(r+c)
        negativeD.remove(r-c)
        board[r][c] = ""


backtrack(0, n, res, board, col, positiveD, negativeD)
for row in res:
    print(row)
