# Diff b/w regular methods , class methods and static methods

# Regular methods are instance methods
# Class methods are methods that are called on a class rather than an instance of the class
# Static methods are methods that are called without creating an instance of the class
# Static methods are used to group utility functions together in a class
class Employee:

    no_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.no_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class Methods
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


emp1 = Employee('zizi', 'anum', 5000)
emp2 = Employee('abc', 'xyz', 6000)


# increase the raise amount
Employee.set_raise_amt(1.05)  # these can even run via instace method
emp1.set_raise_amt(1.08)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
