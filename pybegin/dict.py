#key value pairs
student ={'name': 'john','age':25,'courses':['math','compsci']}

# student['phone']='555-5555'

# print(student['courses'])
# print(student.get('name'))
# print(student.get('phone'))

# student['name']='Jane'

# student.update({'name':'jane','age':26,'phone':'555-5555'})
# #defalut values for keys that don't exist

# del student['age']
# agr = student.pop('age')
# print(student.get('phone','Not Found'))
print(student.keys())

print(student.values())

print(student.items())

for key,value in student.items():
    print(key,value)