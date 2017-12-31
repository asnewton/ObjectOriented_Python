class Employee:
    raise_amt = 1.04
    no_of_emp = 0

    def __init__(self, firstName, lastName, sex, age, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.sex = sex
        self.age = age
        self.pay = pay
        self.email = firstName + '.' + lastName + '@email.com'

        Employee.no_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        firstName, lastName, sex, age, pay = emp_str.split('-')
        return cls(firstName, lastName, sex, age, pay)

    @staticmethod
    def is_workday(weekday):
        if weekday == 5 or weekday == 6:
            return False
        return True


"""operation on class Employee"""

emp_1 = Employee('Ahmad', 'Ashraf', 'Male', 22, 100000)
emp_2 = Employee('Falak', 'Ahmad', 'Female', 21, 80000)

print(Employee.raise_amt)

Employee.set_raise_amt(1.10)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

str_1 = 'Mohd-Ahmad-Male-22-100000'
str_2 = 'Falak-Ahmad-Female-21-80000'

firstName, lastName, sex, age, pay = str_1.split('-')
firstName, lastName, sex, age, pay = str_2.split('-')

new_str_1 = Employee.from_string(str_1)
new_str_2 = Employee.from_string(str_2)
print(new_str_1.email)
print(new_str_1.firstName)
print(new_str_2.firstName)
print(new_str_2.pay)

import datetime
my_date = datetime.date(2017,12,23)

print(Employee.is_workday(my_date))

