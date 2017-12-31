""" How to create class in python """


class Employee:

    def __init__(self, name, age, gender, salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.email = name + "@company.com"

    def fullname(self):
        return '{}'.format(self.name)

Emp_1 = Employee("Ahmad_Ashraf", 22, "male", 100000 ) #instance of class Employee
print(Emp_1.fullname())
print(Emp_1.email)

