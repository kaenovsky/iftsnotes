# Private Access Modifiers
# https://www.codecademy.com/courses/python-for-programmers/articles/access-modifications-python

class ClassSchedule:
    def __init__(self, course, instructor):
        self.__course = course # private
        self.__instructor = instructor # private

    def display_course(self):
        # this method is public
        print(f'course: {self.__course}, instructor: {self.__instructor}')

sched = ClassSchedule('History', 'Ms. Hua')
# sched.__course # error, private attribute
sched.display_course() # no error (method is public)