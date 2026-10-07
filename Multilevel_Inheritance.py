#Multilevel Inheritance : Employee Managment System 

class Person:

    def get_person(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):

    def get_employee(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


class Manager(Employee):

    def get_manager(self, department):
        self.department = department

    def display_manager(self):
        print("Department:", self.department)

manager = Manager()

manager.get_person("Harshad", 25)
manager.get_employee(101, 50000)
manager.get_manager("Computer Engineering")

manager.display_person()
manager.display_employee()
manager.display_manager()