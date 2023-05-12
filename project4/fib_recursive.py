# Names: Kelsey Dang, Adam Sellers, Brian Escobar
# Due Date: 5/12/23
# Filename: fib_recursive.py
# Project 4 Fibonacci Exhaustive Pattern

print("Algorithm 1A: Fibonacci Recursion\n")

# function: input n as parameter
def fib_recursive(n):
    # base cases: first and second term is known
    if n == 0: # if input is 0
        return n
    elif n == 1: # if input is 1
        return n
    else:
        # recursive call by getting two previous values
        return (fib_recursive(n - 1) + fib_recursive(n - 2))

n = int(input("Enter integer for nth term: ")) # user inputs an integer
output = fib_recursive(n) # function call
print("Position", n, "of fibonacci sequence: ", output) # print output
