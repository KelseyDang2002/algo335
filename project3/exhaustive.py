# Name: Kelsey Dang
# Due Date: 4/21/23
# Filename: exhaustive.py
# Project 3 Exhaustive Search Algorithm

print("Algorithm 1: Exhaustive Search\n")

# input: a r x c matrix F, where each cell is either passable or impassable (X);
# and F[0][0] = .
#
# . . . . . . x . x
# x . . . . . . . .
# . . . x . . . x .
# . . x . . . . x .
# . x . . . . x . .
# . . . . x . . . .
# . . x . . . . . x
# . . . . . . . . .
#
# output: the number of different paths starting at (0,0) and ending at (r-1,c-1);
# where each step is either start, right move, or down move; and does not visit any X cell

r = int(input("Enter number of rows: "))
c = int(input("Enter number or columns: "))

matrix = []

print("")
for i in range(r):
    arr = []
    for j in range(c):
        print("Enter . or x for [", i,"][", j, "]: ", end = "")
        arr.append(input())
    matrix.append(arr)

print("\nMatrix: ")
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = " ")
    print("")

# soccer_exhaustive(F):
#     len = r + c - 2
#     counter = 0
#     for bits from 0 to ((2^len) - 1) inclusive:
#         candidate = empty list of moves
#         for k from 0 to (len - 1) inclusive:
#             bit = (bits >> k) & 1
#             if bit == 1:
#                 candidate.add(right)
#             else:
#                 candidate.add(down)
#         if start or end location blocked:
#             return 0
#         if candidate stays inside grid, never crosses an X cell, and ends at (r-1,c-1):
#             counter++
#     return counter
