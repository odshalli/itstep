class Student:
    def __init__(self, height = 200):
        self.height = height

first_student = Student()
mixail = Student(height=150)
Student.__init__(self=first_student)
print(first_student.height)
print(mixail.height)