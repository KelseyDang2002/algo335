# Names: Kelsey Dang, Adam Sellers, Brian Escobar
# Due Date: 5/12/23
# Filename: fib_golden_ratio.py
# Project 4 Fibonacci Golden Ratio Approach

from math import sqrt

print("Algorithm 1B: Fibonacci Golden Ratio\n")

# Get positive integer for variable
def get(x):
    while (True):
        x = input("Please enter a positive integer: ")
        if (x.isdigit() == True and int(x) > 0):
            break
        print(f"{x} is not a positive integer.")
    return int(x)

# Fast Equation 3
def equ3(n):
    rad5 = sqrt(5)
    Fn = ((1 + rad5) ** n)
    Fn -= ((1 - rad5) ** n)
    Fn /= ((2**n)*rad5)
    return Fn

# Fast Equation 4
def equ4(Fp, phi, n, p):
    Fn = Fp * (phi ** (n-p))
    return Fn

# Fast Equation 5
def equ5(Fn, phi):
    Fn *= phi
    return Fn

# Golden Function
def golden():
    # Variable Setup
    phi = 1.61803398875         # Phi = Golden ratio
    p, n = -1, -1               # p = previous position, n = current position
    p = get(p)                  # pos int check for p
    n = get(n)                  # pos int check for n
    outputs_4, outputs_5 = list(), list()

    # PART A - GET Fn USING Fp AND EQUATION 4
    print("\n - PART A -\n")

    Fp = equ3(p)                # Use equation 3 to obtain Fp
    Fn = equ4(Fp, phi, n, p)    # Use equation 4 to obtain Fn
    print(f"Given p = {p},\nand n = {n},\nFp = {Fp},\nFn = {Fn}")

    # PART B - PRINT FIRST 20 TERMS USING EQUATIONS 4 AND 5
    print("\n - PART B -\n")

    print("EQUATION 4\n")
    for i in range(20):
        Fn = equ4(Fn, phi, n+i, n-1+i)
        outputs_4.append(Fn)
        print(f"{Fn}")

    print("\nEQUATION 5\n")
    Fn = equ3(n)
    for i in range(20):
        Fn = equ5(Fn, phi)
        outputs_5.append(Fn)
        print(f"{Fn}")

    # PART C - COMPARISON OF OUTPUTS FROM BOTH EQUATIONS
    print("\n - PART C -\n")
    print("# | equation 4       | equation 5")
    for i in range(20):
        print(f"{i} | {outputs_4[i]} | {outputs_5[i]}")

    # PART D - TESTING THE MAXIM
    print("\n - PART D -\n")
    Fof2 = equ3(2)
    Fof3 = equ5(Fof2, phi)
    Fof29 = equ3(29)
    Fof30 = equ5(Fof29, phi)
    print(f"F3 / F2 = {Fof3 / Fof2}")
    print(f"F30 / F29 = {Fof30 / Fof29}")
    print(f"As n approaches infinity, the ratio of subsequent values in the sequence will approach phi (the golden ratio) thus proving the maxim")

# Driver Code
golden()
