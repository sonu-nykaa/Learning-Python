"""

A library charges a fine for every book returned late. For first 3 days the fine is 10 rupees, for 4-10 days fine
is 20 rupees and above 10 days fine is 50 rupees. If book is returned after 30 days membership will be cancelled.

Write a program that will receive the number of days the member is late to return the book as input and display the
fine or the appropriate message.

"""

fine = 0

days = int(input("Enter days  : "))

if days > 30:
    print("Membership cancelled")
elif days > 10:
    fine = 50
elif days >= 4:
    fine = 20
else:
    fine = 10



