class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@emial.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

emp_1 = Employee('ahmad', 'ashraf')
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'falak ahmad'

print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)

