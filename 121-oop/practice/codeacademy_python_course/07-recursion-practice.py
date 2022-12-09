# A Recursive Function 
# https://www.codecademy.com/courses/python-for-programmers/articles/recursion-in-python

def factorial(num):
    call_stack = []
    if num == 1:
        print('Base case reached, num is 1.')
        return 1
    else:
        call_stack.append({'input': num})
        print('Call stack: ', call_stack)
        return num * factorial(num-1)

print(factorial(5))