"""
Slicing of a List in Python

    In Python, it is possible to access a section of items from the list using the slicing operator

    The format for list slicing is [start:stop:step].
       - start is the index of the list where slicing starts.
       - stop is the index of the list where slicing ends.
       - step allows you to select nth item within the range start to stop.

"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# Get all the Items
print(my_list[:])

# Get all the Items After a Specific Position
print(my_list[2:])

# Get all the Items Before a Specific Position
print(my_list[:2])

# Get all the Items from One Position to Another Position
print(my_list[2:4])

# Get the Items at Specified Intervals
my_list = [1, 2, 3, 4, 5]

print(my_list[::2])
# If you want to get elements at specified intervals, you can do it by using two :. In the above example,
# the items at interval 2 starting from index 0 are sliced.


# If you want the indexing to start from the last item, you can use negative sign -.
my_list = [1, 2, 3, 4, 5]

print(my_list[::-2])
