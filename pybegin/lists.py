courses = ['History', 'math','phy','compsci']
courses_2 = ['Education']
courses.append('Art')
courses.insert(0,'craft')
courses.extend(courses_2)

courses.remove('History')
courses.pop()# use as stack remove last integer

print(courses)
print(courses.index('math'))
print('Art' in courses)


# sort list
courses.reverse()

nums=[1,5,2,4,3]
courses.sort()
courses.sort(reverse=True)
nums.sort()
nums.sort(reverse=True)

sort_course= sorted(courses)

for index,course in enumerate(courses,start=0):
    print(index,course)

course_str = ','.join(courses)
print(course_str)

new_list = course_str.split(',')
print(new_list)