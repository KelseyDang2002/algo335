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

# r = int(input("\tEnter number of rows: ")) # row input
# c = int(input("\tEnter number or columns: ")) # column input
#
# matrix = [] # initialize matrix
#
# print("\nCreate", r, "x", c, "matrix by entering . or x")
# print("for each cell separated by white spaces:\n")
#
# for i in range(r): # loop rows
#     arr = list(input().split()) # input . or x for cells of matrix row by row
#     matrix.append(arr) # append to arr (row-line for matrix)
#
# print("\nMatrix: ")
#
# for i in range(r): # loop rows
#     for j in range(c): # loop columns
#         print(matrix[i][j], end = " ") # print each cell of matrix
#     print("") # print empty space
#
# def soccer_dynamic(matrix, r, c):
#     # corner case: initial cell is impassable
#     if matrix[0][0] == 'x':
#         return 0
#     A = []
#     # base case
#     # A[0][0] = 1
#     # general cases
#     for i in range(0, (r - 1) + 1):
#         for j in range(0, (r - 1) + 1):
#             if matrix[i][j] == 'x':
#                 A[i][j] = 0
#                 continue
#             above = left = 0
#             if i > 0 and matrix[i - 1][j] == '.':
#                 above = A[i - 1][j]
#             if j > 0 and matrix[i][j - 1] == '.':
#                 left = A[i][j - 1]
#             A[i][j] += above + left
#     return A[r - 1][c - 1]
#
# soccer_dynamic(matrix, r, c)

def findPaths(m, path, i, j):
    r = len(m)
    c = len(m[0])
    if i == r-1 and j == c-1:
        print(path+[m[i][j]])
        return

    path.append(m[i][j])

    if m[i][j] != 'x':
        if 0 <= i+1 <= r-1 and 0 <= j <= c-1:
            findPaths(m, path, i+1, j)

        if 0 <= i <= r-1 and 0 <= j+1 <= c-1:
            findPaths(m, path, i, j+1)

    path.pop()

matrix = []
r = int(input("\tEnter number of rows: ")) # row input
c = int(input("\tEnter number or columns: ")) # column input

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

print("\n", end = "")

path = []
findPaths(matrix, path, 0, 0)
