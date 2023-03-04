# Name: Kelsey Dang
# Due Date: 3/19/23
# Filename: p2a1.py
# Project 2 Algorithm 1

print("Algorithm 1\n")

# menu of options for the sample input + 3 extra in docx file
print("Option 1:")
print("arr_A = ['thismetoaklandrialtofullertonmarcolongchinofresnovallejoclovissimithound']")
print("arr_B = ['marco', 'clovis', 'rialto', 'oakland']")

print("\nOption 2:")
print("arr_A = ['sanoaklandrialtofullertonmarcolongbreacoronamodestoclovissimithousand']")
print("arr_B = ['brea', 'modesto', 'clovis', 'corona']")

print("\nOption 3:")
print("arr_A = ['marcopolmonafremontrialtofullertonmarcolongfresnochinoclovissimisalinas']")
print("arr_B = ['fullerton', 'chino', 'fremont', 'fresno']")

print("\nOption 4:")
print("arr_A = ['torranceoaklandrialtomarcooxnardchinofresnoirvineclovissimiorange']")
print("arr_B = ['oxnard', 'irvine', 'orange', 'marco']")

option = int(input("\n\tSelect option (1-4): ")) # user chooses option to run algorithm on

# define arrays
order_array = []
output_array = []
temp_array = []

# set arr_A and arr_B depending on what user chooses
if (option == 1):
    arr_A = ["thismetoaklandrialtofullertonmarcolongchinofresnovallejoclovissimithound"]
    arr_B = ['marco', 'clovis', 'rialto', 'oakland']
elif (option == 2):
    arr_A = ["sanoaklandrialtofullertonmarcolongbreacoronamodestoclovissimithousand"]
    arr_B = ['brea', 'modesto', 'clovis', 'corona']
elif (option == 3):
    arr_A = ["marcopolmonafremontrialtofullertonmarcolongfresnochinoclovissimisalinas"]
    arr_B = ['fullerton', 'chino', 'fremont', 'fresno']
elif (option == 4):
    arr_A = ["torranceoaklandrialtomarcooxnardchinofresnoirvineclovissimiorange"]
    arr_B = ['oxnard', 'irvine', 'orange', 'marco']
else:
    print("Invalid option\n")

# function
def Algorithm1(arr_A, arr_B):
    for city in arr_B: # loop cities in arr_B
        if city in arr_A[0]: # if city is in arr_A
            index = arr_A[0].index(city) # get index where city shows up in arr_A
            pair = [index, city] # group index and city in a pair array
            temp_array.append(pair) # append pair to a temporary array
        else:
            print("element not in arr_A") # if city is not in arr_A
            break

    temp_array.sort() # sort the temporary array by index where city appears in arr_A

    for index, city in temp_array: # loop temporary array
        order_array.append(index) # append the index to order_array
        output_array.append(city) # append city to output_array

    # display order_array and output_array
    # both arrays should be ordered by appearance in arr_A
    print("\norder_array = ", order_array)
    print("output_array = ", output_array)

Algorithm1(arr_A, arr_B) # function call
