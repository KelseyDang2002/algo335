# Name: Kelsey Dang
# Due Date: 3/19/23
# Filename: p2a2.py
# Project 2 Algorithm 2

print("Algorithm 2\n")

string = input("\tEnter a string: ")

print("\nInput string: ", string)

output_string = ""

# function
def Algorithm2(string, output_string):
    string.split() # separate characters from whitespaces - O(n)

    for i in string: # loop through each character in string
        if (i not in output_string):
            num = string.count(i) # count number of characters - O(n)

            if (num >= 2):
                output_string += str(num) # add count of characters to output string - O(n^2)
                output_string += i # add character to output string

            if (num == 1):
                output_string += i # add character to output string

    print("Output string: ", output_string) # print output string

Algorithm2(string, output_string) # function call
