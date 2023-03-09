# Name: Kelsey Dang
# Due Date: 3/19/23
# Filename: p2a2.py
# Project 2 Algorithm 2

print("Algorithm 2\n")

string = input("\tEnter a string: ")

print("\nInput string: ", string)

output_string = ""

# test
# C = 2
# res = []
# curr, cnt = None, 0
#
# for chr in string:
#     if chr == curr:
#         cnt += 1
#     else:
#         curr, cnt = chr, 1
#
#     if chr == C:
#         res.append(C * chr)
#
# print("Output: " + str(res))

# function
def Algorithm2(string, output_string):
    string.split() # separate characters from whitespaces

    for i in string: # loop through each character in string
        if (i not in output_string):
            num = string.count(i) # count number of characters

            if num == 1: # if only 1 character
                output_string += i # add character to output string

            if num > 1: # if 2 or more characters
                output_string += str(num) # add count of characters to output string
                output_string += i # add character to output string

    print("Output string: ", output_string) # print output string

Algorithm2(string, output_string) # function call
