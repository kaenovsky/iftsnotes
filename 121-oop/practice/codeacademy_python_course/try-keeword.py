# https://www.codecademy.com/courses/python-for-programmers/articles/error-handling-in-python
# using try except & finally for error handling

numbs = [0, 1, 2, 3] # not error
# numbs = ['x','y','z'] # error

try:
    print(sum(numbs))
except:
    print('Cannot print the sum! Your variables are not numbers.')
finally:
    print('Hope you got the result you want!')