class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('zizi', 'anum', 5000)
emp2 = Employee('abc', 'xyz', 6000)

print(emp1.first)
print(emp2.email)
print(emp1.fullname())
print(emp2.fullname())
print(Employee.fullname(emp2))
