# Name: Kelsey Dang
# Due Date: 3/19/23
# Filename: p2a2.py
# Project 2 Algorithm 2

print("Algorithm 2\n")

string = input("\tEnter a string: ") # user inputs a string

print("\nInput string: ", string) # print user input

# function
def Algorithm2(string):
    output_string = "" # define output string
    i = 0 # index i starting at 0

    while (i <= len(string) - 1): # while loop when i <= string length - 1 - O(n)
        count = 1 # count starting at 1
        char = string[i] # char is the letter at position i of string
        j = i # set index i equal to index j

        while (j < len(string) - 1): # while loop when j < string length - 1 - O(n)
            if (string[j] == string[j + 1]): # if char is the same as next char then count
                count = count + 1 # increment count by 1
                j = j + 1 # increment index j by 1
            else:
                break

        if (count == 1): # if only 1 char is counted
            output_string = output_string + char # append the char into output string
            i = j + 1 # incremnt index i by 1

        if (count >= 2): # if 2 or more char counted in a row
            # append the number of chars counted and the corresponding char right after
            # into output string
            output_string = output_string + str(count) + char # str() = O(m*n) or O(n^2)
            i = j + 1 # increment index i by 1

    return output_string

output_string = Algorithm2(string) # function call
print("Output string: ", output_string) # print output string
