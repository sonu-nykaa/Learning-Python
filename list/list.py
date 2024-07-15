# In Python, lists allow us to store a sequence of items in a single variable.

# Create a Python List
ages = [19, 26, 29]
print(ages)

# In Python, lists can store data of different data types.
student = ['Jack', 32, 'Computer Science']
print(student)

# an empty list
empty_list = []
print(empty_list)

# Using list() to Create Lists
# We can use the built-in list() function to convert other iterables (strings, dictionaries, tuples, etc.) to a list.
x = "axz"

# convert to list
result = list(x)

print(result)  # ['a', 'x', 'z']

"""
List Characteristics

    Lists are:
        - Ordered - They maintain the order of elements.
        - Mutable - Items can be changed after creation.
        - Allow duplicates - They can contain duplicate values.
        
"""

# Access List Elements

languages = ['Python', 'Swift', 'C++']

# access the first element
print(languages[0])  # Python

# access the third element
print(languages[2])  # C++

# Python also supports negative indexing. The index of the last element is -1, the second-last element is -2, and so on.
# Negative indexing makes it easy to access list items from last.

print(languages[-1])   # C++
print(languages[-3])   # Python

# List of lists
name = ['Sonu', 'Sagar', 'Rahul']

student_ages = [name, ages]
print(student_ages)