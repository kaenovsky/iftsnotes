# Sets in Python
# https://www.codecademy.com/courses/python-for-programmers/articles/sets-in-python

set1 = {'Jenny', 26, 'Parker', 10.5}
print(set1)

# values can't repeat

values = ['Josh', 21, 'Parker', 'Parker', 12.5]
set2 = set(values)
print(set2) # only one 'Parker'

students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dimitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}
print('Chau' in students) # True

students.add('George')
print(students)

students.update(students2) # Amy and Jane won't be added

students3 = students.union(students2)

print(students3)

students.remove('Chau')
print(students)

count_down = set([9, 8, 7, 6, 5, 4, 3, 2, 1])

for num in count_down:
    print(num, 'seconds left!')