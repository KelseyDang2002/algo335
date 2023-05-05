# Names: Kelsey Dang, Adam Sellers, Brian Escobar
# Due Date: 5/12/23
# Filename: largest_sum.py
# Project 4 Largest Sum Subarray Problem

# Sample Inputs:
# (-3, -5, 5, -1, -3, 1, 5, -6)
# (10, 2, -5, 1, 9, 0, -4, 2, -2)
# (-7, 1, 8, 2, -3, 1)
# (9, 7, 2, 16, -22, 11)
# (6, 1, 9, -33, 7, 2, 9, 1, -3, 8, -2, 9, 12, -4)

from sys import maxsize

print("Algorithm 2: Largest Sum Subarray\n")

V = [int(i) for i in input("Enter integers for array: ").split()]
n = len(V)
print("Input =", V)

# function: input V and lenth of V (n) as parameters
def largest_sum(V, n):
    max_curr = -maxsize - 1 # calculate current largest sum
    max_end = 0 # max sum of integers as it loops
    b = 0 # beginning index of largest sum
    e = 0 # ending index of largest sum
    start = 0
    subarray = [] # subarray

    # loop through array V
    for i in range(0, n):
        max_end += V[i] # calculate max of consecutive integers in V
        if max_curr < max_end: # if max_end greater than current largest sum
            max_curr = max_end
            b = start # set beginning index of largest sum
            e = i # set ending index of largest sum
        if max_end < 0: # if max_end is negative
            max_end = 0 # reset max_end to 0
            start = i + 1 # increment start

    # append integers from index b to e in V into subarray
    for i in range(b, e + 1):
        subarray.append(V[i])

    print("Output =", subarray) # print output array
    print("Largest sum =", max_curr) # print largest sum

largest_sum(V, n) # function call
