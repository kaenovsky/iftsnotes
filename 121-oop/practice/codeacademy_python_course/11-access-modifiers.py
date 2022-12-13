# Access Modifications
# https://www.codecademy.com/courses/python-for-programmers/articles/access-modifications-python

# Public Access Modifiers (default)

class ClassSchedule:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor

    def display_course(self):
        print(f'Course: {self.course}, Instructor: {self.instructor}')

# All members here are accessible outside of the class.

sched = ClassSchedule('Math', 'Mr. Xin')
sched.display_course()