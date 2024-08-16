"""
Python Tuple count()
    - The count() method returns the number of times the specified element appears in the tuple.
    - The syntax of the count() method is:  tuple_name.count(element_to_count)
    - The count() method returns:
        > a number of times the given element i is present in the tuple
    - We can also use count() to Count List and Tuple Elements Inside Tuple

"""

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'i', 'u')

# counts the number of i's in the tuple
count = vowels.count('i')

print(count)

# tuple of numbers
numbers = (1, 3, 4, 1, 6, 1)

# counts the number of 1's in the tuple
count = numbers.count(1)

print('The count of 1 is:', count)

# tuple containing list and tuples
random = ('a', ('a', 'b'), ('a', 'b'), [3, 4])

# count element ('a', 'b')
count = random.count(('a', 'b'))

print("The count of tuple ('a', 'b') is:", count)


"""
Python Tuple index()
    - The index() method returns the index of the specified element in the tuple.
    - The syntax of the index() method is: tuple.index(element, start_index, end_index)
    - The index() method can take one to three parameters:
        -> element - the item to scan
        -> start_index (optional) - start scanning the element from the start_index
        -> end_index (optional) - stop scanning the element at the end_index  
    - The index() method returns:
        -> the index of the given element in the tuple
        -> ValueError exception if the element is not found in the tuple
"""

# index of 'e' in vowels
index = vowels.index('e')
print('Index of e:', index)

# throws error since 10 is absent in the tuple
index = numbers.index(10)
print('Index of 3:', index)


""" index() With Start and End Parameters """

# alphabets tuple
alphabets = ('a', 'e', 'i', 'o', 'g', 'l', 'i', 'u')

# returns the index of first 'i' in alphabets
index = alphabets.index('i')

print('Index of i in alphabets:', index)

# scans 'i' from index 4 to 7 and returns its index
index = alphabets.index('i', 4, 7)

print('Index of i in alphabets from index 4 to 7:', index)

