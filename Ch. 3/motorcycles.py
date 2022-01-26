# Abbi Kissee 01.20.22
# This program demonstrates how to modify elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles.append('ducati')
# print(motorcycles)
# these two do about the same thing, insert lets you choose a specific position
motorcycles.insert(0, 'ducati')
print(motorcycles)

# how to remove an item in an position with the del statement
del motorcycles[0]
print(motorcycles)

# how to remove an item based on its value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# how to remove an item based on its value using a variable to hold the value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\tA {too_expensive.title()} is too expensive for me.")

# how to append a list you can do this to a pre-existing list or an empty one like shown here
more_motorcycles = []
more_motorcycles.append('honda')
more_motorcycles.append('yamaha')
more_motorcycles.append('suzuki')
print(more_motorcycles)

# how to use the pop() method using variables to hold the values
popped_motorcycle = more_motorcycles.pop()
print(more_motorcycles)
print(popped_motorcycle)

# how to use the pop() method and insert it into a print statement
more_motorcycles = []
more_motorcycles.append('honda')
more_motorcycles.append('yamaha')
more_motorcycles.append('suzuki')
print(more_motorcycles)
last_owned = more_motorcycles.pop(0)
print(f"The first motorcycle I owned was a {last_owned.title()}.")
