#Multiple Inheritance : Student result System

class Student:
    def student_details(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_student(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)


class Marks:
    def get_marks(self, python, java):
        self.python = python
        self.java = java

    def display_marks(self):
        print("Python Marks:", self.python)
        print("Java Marks:", self.java)


# Child class
class Result(Student, Marks):

    def calculate_result(self):
        total = self.python + self.java
        percentage = total / 2

        print("Total Marks:", total)
        print("Percentage:", percentage)


# Object
student = Result()

student.student_details("Harshad", 101)
student.get_marks(85, 90)

student.display_student()
student.display_marks()
student.calculate_result()