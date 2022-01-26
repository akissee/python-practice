# Abbi Kissee
# 01.26.22

# The order of the list is permanently changed with the sort() method
cars = ['bmw', 'audi', 'toyota', 'suburu']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'suburu']
cars.sort(reverse=True)
print(cars)

# The order of the list is temporarily changed here.
print("\nHere is the temporarily sorted list: ")
print(sorted(cars))
print("\nHere is the original list: ")
print(cars)
print("\n")

# The order is permanently reversed from the order entered.
cars = ['bmw', 'audi', 'toyota', 'suburu']
print(cars)

cars.reverse()
print(cars)
