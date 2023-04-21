# Names: Kelsey Dang, Adam Sellers, Brian Escobar
# Due Date: 4/21/23
# Filename: exhaustive.py
# Project 3 Exhaustive Search Algorithm

import bitstring

print("Algorithm 1: Exhaustive Search\n")

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

# exhaustive search function
def soccer_exhaustive(matrix, i, j, r, c):
    length = r + c - 2
    counter = 0
    for bits in range(0, 2**length):
        candidate = []
        for k in range(0, length):
            bit = (bits >> k) & 1
            if bit == 1:
                candidate.append(1)
            else:
                candidate.append(0)
        if  i == r-1 and j == c-1:
            counter += 1
    return print(counter)

print("\nPaths found: ", end = "")
soccer_exhaustive(matrix, i, j, r, c) # function call
