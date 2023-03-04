# Name: Kelsey Dang
# Due Date: 3/19/23
# Filename: p2a1.py
# Project 2 Algorithm 1

print("Algorithm 1\n")

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

option = int(input("\n\tSelect option (1-4): "))

order_array = []
output_array = []
temp_array = []

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

def Algorithm1(arr_A, arr_B):
    for city in arr_B: # O(n)
        if city in arr_A[0]:
            index = arr_A[0].index(city) #O(n)
            pair = [index, city]
            temp_array.append(pair)
        else:
            print("element not in arr_A")
            break

    temp_array.sort() # O(n*log(n))

    for index, city in temp_array: # O(n)
        order_array.append(index)
        output_array.append(city)

    # print("\ntemp_array = ", temp_array)
    print("\norder_array = ", order_array)
    print("output_array = ", output_array)

Algorithm1(arr_A, arr_B) # O(n^2) <- worst case
