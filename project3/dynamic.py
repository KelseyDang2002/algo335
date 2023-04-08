# Name: Kelsey Dang
# Due Date: 4/21/23
# Filename: dynamic.py
# Project 3 Dynamic Programming Algorithm

print("Algorithm 2: Dynamic Programming\n")

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

r = int(input("\tEnter number of rows: ")) # row input
c = int(input("\tEnter number or columns: ")) # column input

matrix = [] # initialize matrix

print("\nCreate", r, "x", c, "matrix by entering . or x")
print("for each cell separated by white spaces:\n")

for i in range(r): # loop rows
    arr = list(input().split()) # input . or x for cells of matrix row by row
    matrix.append(arr) # append to arr (row-line for matrix)

print("\nMatrix: ")

for i in range(r): # loop rows
    for j in range(c): # loop columns
        print(matrix[i][j], end = " ") # print each cell of matrix
    print("") # print empty space

# soccer_dynamic(F):
#     # corner case: initial cell is impassable
#     if F[0][0] == X:
#         return 0
#     A = new r x c matrix initialized to zeroes
#     # base case
#     A[0][0] = 1
#     # general cases
#     for i from 0 to r-1 inclusive:
#         for i from 0 to c-1 inclusive:
#             if F[i][j] == X:
#                 A[i][j] = 0
#                 continue
#             above = from_left = 0
#             if i > 0 and F[i-1][j] == .:
#                 above = A[i-1][j]
#             if j > 0 and F[i][j-1] == .:
#                 left = A[i][j-1]
#             A[i][j] += above + left
#     return A[r-1][c-1]
