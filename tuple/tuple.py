# Python Tuple
""" A tuple is a collection similar to a Python list. The primary difference is that we cannot modify a
tuple once it is created. """

# Create a Python Tuple

fruits = ('apple', 'cherry', 'orange')
print("Length of Fruits : ", len(fruits))
print(fruits)

# We can also create a tuple using a tuple() constructor. For example,
tuple_constructor = tuple(('Jack', 'Maria', 'David'))
print(tuple_constructor)

# Access Tuple Items
print(fruits[2])  # we can access tuple using index

"""  
Change Tuple Items
    Python Tuples are immutable - we cannot change the items of a tuple once created. If we try to do so, we will get an 
    error. For example,
"""

fruits = ('apple', 'cherry', 'orange')
# trying to change the second item to 'banana'
fruits[1] = 'banana'
print(fruits)
# Output: TypeError: 'tuple' object does not support item assignment

"""  
Delete Tuples
    We cannot delete individual items of a tuple. However, we can delete the tuple itself using the del statement. 
    For example,
"""

animals = ('dog', 'cat', 'rat')
# deleting the tuple
del animals
