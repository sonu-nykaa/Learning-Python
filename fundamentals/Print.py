import keyword

# In Python, anything inside print() is displayed on the screen.
# There are two things to note about print():
#   - Everything we want to display on the screen is included inside the parentheses ().
#   - The text we want to print is placed within double quotes " ".
# We can also use single quotes to print text on the screen.

print("Hello World")
print(1 + 2)
print(10 * 3)
print(10.1 * 3.4)
print("My name is", " sonu", " I am ", 20, " years old")

# Printing in Python
#   print(values, sep, end ) -> will learn about file and flush later
#   values or objects : Any object as many as you like. Will be converted to string before printing
#   sep = 'seperator' : Optional. Specify how to separate the objects, if there is more than one. Default is ''
#   end = 'end' : Optional. Specify what to print at the end. Default is '\n' ( new line )

print("My name is", " sonu", " I am ", 20, " years old", sep='@')
print("After printing this line next print statement will not start on new line but with a dash", end=' -- ')
print("New Sentence")

# Keywords in Python
print("There are total ", len(keyword.kwlist), " in python")
print(keyword.kwlist)
