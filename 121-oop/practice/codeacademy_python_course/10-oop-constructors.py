# Constructors and destructors
# https://www.codecademy.com/courses/python-for-programmers/articles/constructors-and-destructors-python

class ClassSchedule:
    def __init__(self, course):
        self.course = course

    def __del__(self):
        print('You succesfully deleted your schedule')

# first = ClassSchedule('Math')
second = ClassSchedule('Chemistry')

# print(first.course)
del second