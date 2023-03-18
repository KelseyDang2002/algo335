# Names: Kelsey Dang, Adam Sellers, Brian Escobar
# Due Date: 3/19/23
# Filename: p2a3.py
# Project 2 Algorithm 3

print("Algorithm 3\n")

# menu of options from docx file
print("Option 1:")
print("all_lists = [ [2, 5, 9, 21], \n[-1, 0, 2], \n[-10, 81, 121], \n[4, 6, 12, 20, 150] ]")

print("\nOption 2:")
print("all_lists = [ [10, 17, 18, 21, 29], \n[-3, 0, 3, 7, 8, 11], \n[81, 88, 121, 131], \n[9, 11, 12, 19, 29] ]")

print("\nOption 3:")
print("all_lists = [ [-4, -2, 0, 2, 7], \n[4, 6, 12, 14], \n[10, 15, 25], \n[5, 6, 10, 20, 24] ]")

option = int(input("\n\tSelect option (1-3): ")) # user chooses option to run algorithm on

# Define Test Case
if (option == 1):
    all_lists =[ [2, 5, 9, 21],
    [-1, 0, 2],
    [-10, 81, 121],
    [4, 6, 12, 20, 150] ]
elif (option == 2):
    all_lists = [ [10, 17, 18, 21, 29],
    [-3, 0, 3, 7, 8, 11],
    [81, 88, 121, 131],
    [9, 11, 12, 19, 29] ]
elif (option == 3):
    all_lists = [ [-4, -2, 0, 2, 7],
    [4, 6, 12, 14],
    [10, 15, 25],
    [5, 6, 10, 20, 24] ]
else:
    print("Invalid option\n")

# Merge the lists into one master list O(n)
def list_merge(list_of_lists):
    result = []
    for list in list_of_lists:
        result += list
    return result

# Standard heapify methond O(log(n)) - max heap
def heap_sort(list, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Check if left is larger than root
    if l < n and list[i] < list[l]:
        largest = l

    # Check if right is larger than current largest
    if r < n and list[largest] < list[r]:
        largest = r

    # Swap root if new elements are larger
    if largest != i:
        (list[i], list[largest]) = (list[largest], list[i])

    # Recursion: heap_sort with the new root
        heap_sort(list, n, largest)

# Main function to create the heap using heap_sort O(n*log(n))
def heap_create(list):
    n = len(list)

    for i in range(n // 2 - 1, -1, -1): #n//2 - 1 =
        heap_sort(list, n, i)

    for i in range(n - 1, 0, -1): # Iterate through max heap in reverse
        (list[i], list[0]) = (list[0], list[i]) # swap list[0] and list[1]
        heap_sort(list, i, 0)

# Driver
master_list = list_merge(all_lists)
heap_create(master_list)
print("\nSorted output: ", master_list)
