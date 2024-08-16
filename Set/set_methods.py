"""
Add Items to a Set in Python
    - In Python, we use the add() method to add an item to a set. For example,
"""

numbers = {21, 34, 54, 12}
print('Initial Set:', numbers)

# using add() method
numbers.add(32)
print('Updated Set:', numbers)

"""
Update Python Set
    - The update() method is used to update the set with items other collection types (lists, tuples, sets, etc). For example,
"""
animals = {"Dog", "Cat", "Rabbit", "Tiger"}
wild_animals = ["Lion", "Wolf", "Leopard", "Tiger"]

# using update() method
animals.update(wild_animals, {"Turtle"})
print(animals)

"""
Remove an Element from a Set
    - We use the discard() / remove() method to remove the specified element from a set. 
        -> If we are trying to remove any element which is not present in set using remover() method then it will throw 
           error whereas discard() method will not throw any error. 
    - To remove all elements of set we can use clear() method
    
"""
# using discard method
animals.discard("Cat")
print(animals)

# using remove method
animals.remove("Dog")
print(animals)

# Removing element which is not present in set

# 1. Using discard() method
animals.discard("dolphin")

# 2. Using remove() method
animals.remove("dolphin")  # KeyError: 'dolphin'

""" Check if the item is in the set """

