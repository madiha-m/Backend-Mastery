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
        self.pay = int(self.pay * 1.04)  # replacing 1.04 with class var

        # use of class variable instead of hard coding
        # using via class
        self.pay = int(self.pay * Employee.raise_amount)

        # using via class instance self
        self.pay = int(self.pay * self.raise_amount)


print(f'No of Employees Before instance creation: {Employee.no_of_employees}')

emp1 = Employee('zizi', 'anum', 5000)
emp2 = Employee('abc', 'xyz', 6000)

print(f'No of Employees After instance creation: {Employee.no_of_employees}')

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)


# 1- under the cases are not applicable, as raise_amount not defined yet. lets define it as class var
# # What if we want to check raised amount of single employee
# emp1.raise_amount

# # Or get the raised amount of all employees
# Employee.raise_amount

# 2- raise_amount is defined as class var, and applied. now can check its amount
print(Employee.raise_amount)
print(emp1.raise_amount)

print(emp1.__dict__)
print(Employee.__dict__)
