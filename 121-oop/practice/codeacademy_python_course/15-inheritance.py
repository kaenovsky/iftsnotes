# Inheritance
# https://www.codecademy.com/courses/python-for-programmers/articles/inheritance-python

# Parent class:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'The name of this person is {self.name} and their age is {self.age}')

p1 = Person('Luke', 28)
p1.display_info()

# Child class:

class Teacher(Person):
    def __init__(self, name, age, subject):
        self.subject = subject

        Person.__init__(self, name, age)

t1 = Teacher('Xing', 42, 'Art')
t1.display_info()