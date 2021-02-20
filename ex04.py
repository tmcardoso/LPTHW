# Number of cars
cars = 100
# Number of passengers each car can has
space_in_car = 4.0
# Number of people who can drive cars
drivers = 30
# Number of passengers that will need a ride
passengers = 90
# Number of cars that will not have a driver
cars_not_driven = cars - drivers
# Number of cars that will be driven
cars_driven = drivers
# Number of max passengers that all cars driven
# can have in total
carpool_capacity = cars_driven * space_in_car
# Average of passengers that will need a ride per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
    "in each car.")
