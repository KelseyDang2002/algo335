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

for i in arr_B: # O(n)
    if i in arr_A[0]:
        index = arr_A[0].index(i) #O(n)
        city = i
        order_array.append(index)
        output_array.append(city)

order_array.sort() # O(n*log(n)) <- worst case
print("\n\torder_array = ", order_array)
print("\toutput_array = ", output_array)
