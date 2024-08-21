# message = """Hello World"""

# print(len(message)) 
# print(message.count('l'))
# print(message.find('World'))
# print(message.find('world'))

# new_msg=message.replace('World',"Universe")
# print(new_msg)


greeting ='Hello'
name = " Jerin"

# concat
# message = greeting + ', ' + name
message = greeting + ', ' + name

#use format and placeholders
# message = '{}, {}. Welcome'.format(greeting, name)
# or use below
message = f'{greeting}, {name}. Welcome'
print(message)

#use this to find what functions will work with it
print(dir(name))
#use this if u dont want to search online for the same
print(help(str.lower))