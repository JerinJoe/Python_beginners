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
    
    @classmethod #decorator 
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, empstr):
        first, last, pay = empstr.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() ==6:
            return False
        return True
emp_1= Employee('John','brown',60000)
emp_2= Employee('Test','User',50000)

emp_str_1= 'John-Doe-70000'

new_emp_1 = Employee.from_string(emp_str_1)
Employee.set_raise_amount(1.05)

import datetime
my_date =datetime.date(2016,7,11)
print(Employee.is_workday(my_date))