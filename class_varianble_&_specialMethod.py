class Employee:

    raise_amt = 1.04 #class variable

    def __init__(self, fname, lname, pay, company):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.company = company
        self.email = fname + '.' + lname + '@' + company +'.com'

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def apply_raise(self):
        self.pay = int(float(self.pay) * Employee.raise_amt)

    def __repr__(self):                                   #special method
        return "Employee({}-{})".format(self.pay, self.email)

    def __add__(self, other):                             #special method
        return self.pay + other.pay

    def __str__(self):                                    #special method
        return '{} --{}'.format(self.fullname(), self.pay)

    def __len__(self):                                    #special method
        return len(self.fullname())



emp_1 = Employee('falak', 'ahmad', 100000, 'tesla')
emp_2 = Employee('ahmad', 'ashraf', 200000, 'google')

print(emp_1)
print(emp_2)


