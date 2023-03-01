# Names: Kelsey Dang, Adam Sellers, Brian Escobar
# Due Date: 2/26/23
# Filename: p1a1.py
# Project Name: Project 1 Algorithm 1

# define city distance array and fuel array
city_distance_list = []
fuel_list = []

# function for calculating preferred starting city
def path(city_distance_list, fuel_list, miles_per_gallon):

    start = 0 # starting index initially at 0
    shortage = 0 # when value of fuel is negative it is stored in shortage
    fuel = 0 # fuel intially at 0

    for i in range(5):
        fuel += (miles_per_gallon * fuel_list[i]) - city_distance_list[i] # formula
        if (fuel < 0): # if fuel is negative then increment to change starting city
            start = i + 1
            shortage += fuel # calculate shortage
            fuel = 0 # reset car fuel to 0 after changing city

    if (fuel + shortage >= 0): # if fuel + shortage is >= 0 then traverse to next city
        return start
    else:
        return -1 # if there is no solution

print("Algorithm 1\n")

# user enters city distances, fuel, and mpg
city_distance_list = [int(i) for i in input("\tEnter city distances: ").split()]
fuel_list = [int(i) for i in input("\tEnter fuel for each city: ").split()]
miles_per_gallon = int(input("\tEnter miles per gallon: "))

# displays the city_distance_list array, the fuel_list array, and the mpg entered
print("\ndistance: ", city_distance_list)
print("fuel: ", fuel_list)
print("mpg: ", miles_per_gallon)

# function call
result = path(city_distance_list, fuel_list, miles_per_gallon)
if (result == -1):
    print("\nNo possible solution") # if there isn't a solution
else:
    print("\nPreferred starting city = ", result) # prints the solution
