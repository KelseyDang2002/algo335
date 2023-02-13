# Name: Kelsey Dang
# Due Date: 2/25/23
# Filename: p1a1.py
# Project Name: Project 1 Algorithm 1

import time

print("Algorithm 1\n")

city_distance_list = [5, 25, 15, 10, 15]
fuel_gallons = [1, 2, 1, 0, 3]
miles_per_gallon = int(input("Enter mpg (positive integer): "))

# i = number of cities
# num_cities = int(input("Enter the number of cities: "))

# for i in range(1, num_cities + 1):
    # distance = int(input("Enter distance: "))
    # city_distance_list.append(distance)

# print("city_distance_list = ", city_distance_list)
# print("Shortest distance: ", min(city_distance_list))

# best case: minimum distance of next city + maximum next city gallon?

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
pool = cycle(city_distance_list)
for i in pool:
    print(i)
