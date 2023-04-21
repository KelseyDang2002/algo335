# Names: Kelsey Dang, Adam Sellers, Brian Escobar
# Due Date: 4/21/23
# Filename: exhaustive.py
# Project 3 Exhaustive Search Algorithm

print("Algorithm 1: Exhaustive Search\n")
#
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
# # exhaustive search function
# def soccer_exhaustive(matrix, i, j, r, c):
#     length = r + c - 2
#     counter = 0
#     for bits in range(0, 2**length):
#         candidate = []
#         for k in range(0, length):
#             bit = (bits >> k) & 1
#             if bit == 1:
#                 candidate.append(1)
#             else:
#                 candidate.append(0)
#         if  i == r-1 and j == c-1:
#             counter += 1
#     return print(counter)
#
# print("\nPaths found: ", end = "")
# soccer_exhaustive(matrix, i, j, r, c) # function call

# Board Class (for easy debug)
class Board:
    def __init__(self, r, c):
        self.rows = r
        self.columns = c
        self.board = self.empty_board_fill(self.rows, self.columns)

    def empty_board_fill(self, r, c):
        field = [[0 for x in range(c)] for y in range(r)]
        return field

    def player_positions(self, *args):
        for arg in args:
            self.board[arg[0]][arg[1]] = 1

    def display(self):
        for i in range(self.rows):
            print(self.board[i])

def test_case():
    test = Board(8, 9)
    test.player_positions((0,6),(0,8),(1,0),(2,3),(2,7),(3,2),(3,7),(4,1),(4,6),(5,4),(6,2),(6,8))
    test.display()
    return test

# Parameters: candidate is a string od 1s and 0s of length (r+c-2),
# field = 2-D array representing the players as 1s and empty spaces as 0s
def validate_solution(candidate, field):
    # run through the binary string where 0 = right(+1 row), 1 = down(+1 column)
    pos = [0,0]
    for bit in candidate:
        # Check if a move right is valid
        if bit == "0":
            if pos[0]+1 < field.rows:               # inside board check
                pos[0] += 1                         # move right one spot
            if field.board[pos[0]][pos[1]] == 1:    # player collision check
                return False
        # Check if a move down is valid
        else:
            if pos[1]+1 < field.columns:            # inside board checkS
                pos[1] += 1                         # move down one spot
            if field.board[pos[0]][pos[1]] == 1:    # player collision check
                return False
    # Check if final position is [r-1][c-1]
    if pos != [field.rows - 1, field.columns - 1]:
        return False
    return True

def soccer_exhaustive():
    field = test_case()
    size = field.rows + field.columns - 2
    counter = 0

    # Generate Candidate Solutions (binary strings of length (r+c-2))
    candidate_solutions = list()
    for i in range(2**size, 2**(size+1)):
        candidate = (bin(i)[3:])
        if (validate_solution(candidate, field) == True):
            counter += 1

    return counter

# Driver
final_total = soccer_exhaustive()
print(final_total)
