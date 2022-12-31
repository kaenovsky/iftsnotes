# String methods in Python
# https://www.codecademy.com/courses/python-for-programmers/articles/string-methods-in-python

intro = "My name is Jeff!"
intro2 = "Say Goodbye to 2022"
intro3 = "Hello 2023"

# String indexing and Slicing
print(intro[0]) # prints first letter 'M'
print(intro[0:2]) # prints first two letters 'My'
print(intro[-5:-1]) # prints 'Jeff'

print(len(intro)) # 16
print(len(intro2)) # 12
print(len(intro3)) # 10

# str.lower(), str.upper(), str.title()

print(intro2.lower()) # prints 'say goodbye to 2022' 
print(intro2.upper()) # prints 'SAY GOODBYE TO 2022'
print(intro2.title()) # prints 'Say Goodbye To 2022'

# str.split()

print(intro.split()) # prints array ['My', 'name', 'is', 'Jeff!']
print(intro.split('name')) # prints ['My ', ' is Jeff!']
print(intro.split('!')) #prints ['My name is Jeff', '']