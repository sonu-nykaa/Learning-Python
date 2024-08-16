class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


stud1 = Student("Sonu", 90)
# stud1.name = "Sonu Ray"
# stud1.marks = 90

print(stud1.name)

# did_pass = stud1.check_pass_fail()
# print(did_pass)

stud2 = Student()
stud2.name = "Sagar"
stud2.marks = 35
did_pass = stud2.check_pass_fail()
print(did_pass)
