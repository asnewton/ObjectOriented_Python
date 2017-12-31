
class Employee:

    raise_amt = 1.04

    def __init__(self, fname, lname, sex, pay):
        self.fname = fname
        self.lname = lname
        self.sex = sex
        self.pay = pay
        self.email = fname + '.' + lname + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay =  int(float(self.pay) * self.raise_amt)

class Developer(Employee):  #inheritance

    raise_amt = 1.10

    def __init__(self, fname, lname, sex, pay, pro_lang ):
        Employee.__init__(self, fname, lname, sex, pay)
        self.pro_lang = pro_lang


class Manager(Employee):

    def __init__(self, fname, lname, sex, pay, employee_no = None):
        Employee.__init__(self, fname, lname, sex, pay)
        if employee_no is None:
            self.employee_no = []
        else:
            self.employee_no = employee_no

    def add_emp(self, emp):
        if emp not in self.employee_no:
            self.employee_no.append(emp)

    def remove_emp(self, emp):
        if emp in self.employee_no:
            self.employee_no.remove(emp)

    def print_emp(self):
        for emp in self.employee_no:
            print('--> '+ emp.fullname())


emp_1 = Employee('ahmad', 'ashraf', 'male', 100000)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

dev_1 = Developer('ahmad', 'ashraf', 'male', 100000, 'Python')

print(dev_1.email)
print(dev_1.fullname())
print(dev_1.pro_lang)

mngr_1 = Manager('falak', 'ahmad', 'female', 80000, [emp_1])

print(mngr_1.email)
print(mngr_1.fullname())
print(mngr_1.print_emp())

mngr_1.add_emp(dev_1)
print(mngr_1.print_emp())

mngr_1.remove_emp(emp_1)
print(mngr_1.print_emp())

print(isinstance(mngr_1, Manager))
print(issubclass(Manager, Employee))
print(isinstance(mngr_1, Employee))

