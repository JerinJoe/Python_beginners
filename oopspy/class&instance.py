class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@example.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)


emp_1= Employee('John','brown',60000)

# print(emp_1)
print(emp_1.email)
print(emp_1.fullname())
