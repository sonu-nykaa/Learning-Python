marks = [55, 64, 75, 80, 43]

result = sum(marks)
average = result / len(marks)

if average >= 80:
    print("A")
elif average >= 60:
    print("B")
elif average >= 50:
    print("C")
else:
    print("F")


class Student:
    pass