# Everything is object in python

#  Type() can be used to check the type of data

Test1 = [70, 80, 90, 100]
print(type(Test1))

# To List-out all attributes and methods of a class, we can use dir()
print(dir(Test1))

Test2 = [40, 50, 60, 70]
result = Test1.__add__(Test2)  # Append the list items at the end of 1st list
print(result)

# In python every object has an id for identity. The id of an object is always unique and constant for this object
# during it's lifetime

print(id(Test1))
print(id(Test2))

