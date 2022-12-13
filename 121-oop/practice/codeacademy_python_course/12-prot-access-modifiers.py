# Protected Access Modifiers
# https://www.codecademy.com/courses/python-for-programmers/articles/access-modifications-python

class ClassSchedule:
    def __init__(self, course, instructor):
        self.__course = course # protected
        self.__instructor = instructor # protected

    def display_course(self):
        print(f'Course: {self.__course}, Instructor: {self.__instructor}')

sched = ClassSchedule('Biology', 'Ms. Zhang')
sched.display_course()