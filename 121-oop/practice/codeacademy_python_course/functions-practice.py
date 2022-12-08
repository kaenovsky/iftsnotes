# using functions: 
# https://www.codecademy.com/courses/python-for-programmers/articles/function-basics-python

def sum_three(num1, num2, num3):
    total = num1 + num2 + num3
    return total

print(sum_three(5, 8, 32))

# second example: Parameters

def greetings(language):
    if language == 'spanish':
        greeting = 'hola'
    elif language == 'english':
        greeting = 'hello'
    elif language == 'chinese':
        greeting = 'nihao'

    return greeting

print(greetings('chinese'))