# Names: Kelsey Dang, Adam Sellers, Brian Escobar
# Due Date: 4/21/23
# Filename: dynamic.py
# Project 3 Dynamic Programming Algorithm

import numpy as np

print("Algorithm 2: Dynamic Programming\n")

r = int(input("\tEnter number of rows: ")) # row input
c = int(input("\tEnter number or columns: ")) # column input

matrix = np.zeros((r, c)) # initialize matrix

player_positions = [(0,6),(0,8),(1,0),(2,3),(2,7),(3,2),(3,7),(4,1),(4,6),(5,4),(6,2),(6,8)]

index = np.r_[player_positions].T
matrix[index[0], index[1]] = 1

print("\nMatrix: ")
print(matrix)
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

# function, parameters: matrix, number of rows, number of columns
def soccer_dynamic(matrix, r, c):
    # corner case: initial cell is impassable
    if matrix[0][0] == 1:
        return 0
    A = np.zeros((r, c)) # new r x c matrix initialized to zeroes
    # base case
    A[0][0] = 1
    # general cases
    for i in range(r): # loop rows
        for j in range(c): # loop columns
            if matrix[i][j] == 1: # if position is impassable
                A[i][j] = 0 # position in A matrix = 0
                continue
            above = left = 0 # set above and left = 0
            if i > 0 and matrix[i - 1][j] == 0: # if down position is passable
                above = A[i - 1][j] # valid down move, update A
            if j > 0 and matrix[i][j - 1] == 0: # if right position is passable
                left = A[i][j - 1] # valid right move, update A
            A[i][j] += above + left # add position to A
    return print("\nPaths found: ", A[r - 1][c - 1]) # return number of paths found

soccer_dynamic(matrix, r, c) # function call
