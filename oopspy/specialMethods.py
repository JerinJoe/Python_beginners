class Employee:
    no_of_employees = 0

    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@example.com'

        Employee.no_of_employees += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
    
    def __str__(self) -> str:
        return '{} - {}'.format(self.fullname(),self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
    
emp_1= Employee('John','brown' ,60000)
emp_2= Employee('Test','User',50000)
print(emp_1.__repr__())# used for debugging
print(emp_1.__str__()) # used for end user readability
# print(emp_1)

print(emp_1 + emp_2)