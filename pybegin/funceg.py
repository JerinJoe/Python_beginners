# def hello_func():
#     # print('hello function!')
#     return 'hello function!'

# x=hello_func()
# print(x)

# #DRY: dont repeat yourself

# def hello_func(greeting, name = 'You'):
#     return f'{greeting}, {name}'

# print(hello_func('Hi',name= 'Corey'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


courses = ['Math','Art','History']
info ={'name':'John','age':22 }


# student_info('Math','Art','History',name='John',age=22)

student_info(*courses,**info)