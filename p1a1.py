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

# function for calculating preferred starting city
# def path(city_distance_list, fuel_list, miles_per_gallon, c, f):
#
#     start = 0
#     deficit = 0 # when value of capacity is negative it is stored in deficit
#     capacity = 0
#
#     for i in range(f):
#         capacity += (miles_per_gallon * fuel_list[i]) - city_distance_list[i + 1]
#         if (capacity < 0): # if capacity is negative then increment start
#             start = i + 1
#             deficit += capacity
#             capacity = 0
#
#     if (capacity + deficit >= 0):
#         return start
#     else:
#         return -1

# def path(city_distance_list, fuel_list, miles_per_gallon, c, f):
#
#     for (i, j) in zip(fuel_list, city_distance_list):
#         start_fuel = i
#         start_city = j
#
#         miles = (miles_per_gallon * fuel_list[i])
#         next_city_distance = city_distance_list[i + 1]
#         miles_left = miles - next_city_distance
#
#         return miles_left
#
#         if (miles_left < 0):
#             start_fuel = i + 1
#             start_city = j + 1
#
#         if (miles_left >= 0):
#             return start_fuel, start_city
#         else:
#             return -1

def path(city_distance_list, fuel_list, miles_per_gallon, c, f):

# it literally just if ( gas tank < 0) { start = i + 1/increment the index/ curr fuel = 0;
# /reset the cars gas/ to reset the loop then
# if(totalFuel < 0)
#     return -1
# else
#     return start

    start = 0

    miles = (miles_per_gallon * fuel_list[i])
    next_city_distance = city_distance_list[i + 1]
    miles_left = miles - next_city_distance

    if (miles >= 0):
        return start
    else:
        return -1

# user enters city distances, fuel, and mpg
city_distance_list = [int(i) for i in input("\tEnter city distances: ").split()]
fuel_list = [int(i) for i in input("\tEnter fuel for each city: ").split()]
miles_per_gallon = int(input("\tEnter miles per gallon: "))

print("\ndistance: ", city_distance_list)
print("fuel: ", fuel_list)
print("mpg: ", miles_per_gallon)

result = path(city_distance_list, fuel_list, miles_per_gallon, c, f)
if (result == -1):
    print("\nNo possible solution")
else:
    print("\nPreferred starting city = ", result)
