# An escape sequence is a sequence of characters that, when used inside a character or string, does not
# represent itself but is converted into another character or series of characters that may be difficult or
# impossible to express directly, like newline (\n), tab (\t), and so on.

string1 = "I am \nstring\nin several lines"
print(string1)

string2 = "1. Java \t 2. Python \t 3. JavaScript"
print(string2)

print('Nykaa Leadership told that "It\'s going to be huge".')
#  using multiline string
print("""Nykaa Leadership told that "It's going to be huge".""")

# Python Multiline String
# We can also create a multiline string in Python. For this, we use triple double quotes """ or triple single
# quotes ''. For example,

message = """
Never gonna give you up
Never gonna let you down
"""

print(message)

message = """\
Never gonna give you up \
Never gonna let you down \
"""

print(message)

# C: \Users\temp\new_Course.pdf
print("C: \\Users\\temp\\new_course.pdf")

# Raw String : In Python, a raw string is a special type of string that allows you to include backslashes (\)
# without interpreting them as escape sequences.
print(r"C: \Users\temp\new_course.pdf")

print("Hello \b\b\b\b\bWorld!")
print("Hi Sagar. \rHow are you ? ")

# Number System Escape Sequence -> /ooo for octal values , three o because it needs three values e.g.m \110 -> 72
print("\110\145\154\154\157")
# Decimal value of 110 is 72 and In ASCII table value of 72 is H

# Hexadecimal -> /xhh , two values followed by x
print("\x48\x65\x6c\x6c\x6f\x20")
