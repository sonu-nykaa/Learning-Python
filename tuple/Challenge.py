"""
Write a function to modify a tuple by adding an element at the end of it.
    For inputs with tuple (1, 2, 3) and element 4, the return value should be (1, 2, 3, 4).
    Hint: You need to first convert the tuple to another data type, such as a list.
"""

numbers = (1, 2, 3)

# Converting tuple to list
number_list = list(numbers)
# append 4 in list
number_list.append(4)

# convert number_list to tuple
numbers = tuple(number_list)
print(numbers)