# Name: Kelsey Dang
# Due Date: 2/26/23
# Filename: p1a1.py
# Project Name: Project 1 Algorithm 1

import time
import itertools

print("Algorithm 1\n")

city_distance_list = []
c = len(city_distance_list)
fuel_list = []
f = len(fuel_list)
miles_per_gallon = int(input("Enter mpg (positive integer): "))

print("\n")

for i in range(5):
    city_distance = int(input("\tEnter city distance followed by <enter>: "))
    city_distance_list.append(city_distance)

print("\n")

for i in range(5):
    fuel = int(input("\tEnter available fuel in each city followed by <enter>: "))
    fuel_list.append(fuel)

print("\n")
print(city_distance_list)
print(fuel_list)

def printTour(arr,n):

    # Consider first petrol pump as starting point
    start = 0
    # These two variable will keep tracking if there is
    # surplus(s) or deficit(d) of petrol in the truck
    s = 0          # petrol available the truck till now
    d = 0        # deficit of petrol till visiting this petrol pump

    # Start from the first petrol pump and complete one loop
    # of visiting all the petrol pumps and keep updating s and d at each pump
    for i in range(n):
        s += arr[i][0] - arr[i][1]
        if s < 0:            # the truck has a deficit of petrol
            start = i+1        # change the starting point
            d += s            # storing the deficit of petrol till current petrol pump
            s = 0            # starting again from new station

    # when we reach first petrol pump again and sum of the petrol available at the truck
    # and the petrol deficit till now is 0 or more petrol then return the starting point
    # else return -1
    return start if (s+d)>=0 else -1


# Driver program to test above function
arr = [[6,4], [3,6], [7,3]]
start = printTour(arr,3)
if start == -1:
    print("No Solution Possible !!!")
else:
    print("start = {}".format(start))

# miles = (miles_per_gallon * fuel_gallons[ind])
# next_city_fuel = (miles_per_gallon * fuel_gallons[ind + 1])

# i = number of cities
# num_cities = int(input("Enter the number of cities: "))

# for i in range(1, num_cities + 1):
    # distance = int(input("Enter distance: "))
    # city_distance_list.append(distance)

# print("city_distance_list = ", city_distance_list)
# print("Shortest distance: ", min(city_distance_list))

# best case: minimum distance of next city + maximum next city gallon?
'''
# Method 1 to traverse: circular linked list
# structure for a Node
class Node:
    # constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    # constructor to create an empty circular linked list
    def __init__(self):
        self.head = None

    # function to insert a node at the beginning of a circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head

        # if linked list is not None then set the next of last node
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = ptr1

        else:
            ptr1.next = ptr1 # for the first node

        self.head = ptr1

    # function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print(temp.data, end = "\n")
                time.sleep(1)
                temp = temp.next
                if(temp == self.head):
                    break

# initialize list as empty
cllist = CircularLinkedList()

# created linked list will be 5->25->15->10->15
print("Order of cities according to city_distance_list:\n")
cllist.push(15)
cllist.push(10)
cllist.push(15)
cllist.push(25)
cllist.push(5)

cllist.printList()

# Method 2 to traverse: cycle()
def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element

# loops forever though
# pool = cycle(city_distance_list)
# for i in pool:
#     print(i)

# Method 3 to traverse: circular array
# takes O(n) time but takes O(n) extra space
def prints(a, n, ind):
    # create auxillary array of twice size
    b = [None] * 2 * n
    i = 0

    # copy a[] and b[] two times
    while i < n:
        b[i] = b[n + i] = a[i]
        i = i + 1

    i = ind

    # print from ind-th index to (n+i)th index
    while i < n + ind:
        print(b[i], end = "\n")
        time.sleep(1)
        i = i + 1

# Method 3.1 to traverse: circular array
# circular array without using extra memory space
# takes O(n) time and O(1) extra space
def traverse(a, n, ind):
    i = ind

    while i < n + ind:
        print(a[i % n], end = "\n")
        time.sleep(1)
        i = i + 1

# Driver Code
a = [5, 25, 15, 10, 15]
n = len(a)
miles = (miles_per_gallon * fuel_gallons[ind])
next_city_fuel = (miles_per_gallon * fuel_gallons[ind + 1])
ind = int(input("Enter starting city(0-4): "))
print("Order of cities:\n")
#prints(a, n, ind)
for ind in a:
    if miles + next_city_fuel >= a[ind + 1]:
        traverse(a, n, ind)

    else:
        print("Not enough miles to travel to next city.\n")
        print("Miles left: ", miles + next_city_fuel)
'''
# Program Output
# Algorithm 1
#
# Enter mpg (positive integer): 10
# Order of cities according to city_distance_list:

# 5
# 25
# 15
# 10
# 15
# Enter starting city(0-4): 3
# Order of cities:

# 10
# 15
# 5
# 25
# 15
