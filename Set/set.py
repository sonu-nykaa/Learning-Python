"""
Python Sets
    - A set is a collection of unique data, meaning that elements within a set cannot be duplicated.
        -> Items of set are not in order
        -> no duplicates items are allowed
        -> Item must be immutable objects

"""

""" Create a Set in Python """

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

"""
Create an Empty Set in Python : 
    Creating an empty set is a bit tricky. Empty curly braces {} will make an empty dictionary in Python.
    To make a set without any elements, we use the set() function without any argument. For example,
"""

# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = {}

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary:', type(empty_dictionary))

# We can also use set() to create non-empty set
animals = set(["Cat", "Dog", "Monkey"])
print(animals)

""" Duplicate Items in a Set """
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)  # {8, 2, 4, 6}

# Here, we can see there are no duplicate items in the set as a set cannot contain duplicates.
