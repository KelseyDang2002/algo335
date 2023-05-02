# Name: Kelsey Dang
# Due Date: 5/12/23
# Filename: largest_sum.py
# Project 4 Largest Sum Subarray Problem

# Sample Inputs:
# (-3, -5, 5, -1, -3, 1, 5, -6)
# (10, 2, -5, 1, 9, 0, -4, 2, -2)
# (-7, 1, 8, 2, -3, 1)
# (9, 7, 2, 16, -22, 11)
# (6, 1, 9, -33, 7, 2, 9, 1, -3, 8, -2, 9, 12, -4)

print("Algorithm 2: Largest Sum Subarray\n")

# V = [int(i) for i in input("Enter integers for array: ").split()]
V = [-3, -5, 5, -1, -3, 1, 5, -6]
n = len(V)
print("Input =", V)

def largest_sum(V, n):
    b = V[0]
    e = 0
    S = []
    for i in range(0, n - 1):
        e = e + V[i]
        if e < 0:
            e = 0
        elif e >= 0:
            S.append(V[i])
            b = e
    return S

output = largest_sum(V, n)
print("Output =", output)
