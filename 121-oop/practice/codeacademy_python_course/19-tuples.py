# Tuples in Python
# https://www.codecademy.com/courses/python-for-programmers/articles/tuples-in-python

my_tuple = ('abc', 123, 'def', 456)
my_num_tuple = (34, 2, 650, 19, 2)
my_txt_tuple = ('change', 'drama', 'intensive', 'external', 'drama', 'drama')

# Tuples are capable of holding one item as long as the item is followed by a comma:
my_single_element_tuple = ('one',) 

# Tuple Indexing and Slicing
print(my_tuple[0]) # prints abc

print(my_tuple[1:3]) # prints 123, def

# Common Built-in Functions
print(len(my_tuple))

print(max(my_num_tuple))

print(max(my_txt_tuple))

# error, all elements must be the same type
# print(max(my_tuple)) 

print(min(my_num_tuple))

print(min(my_txt_tuple))

# .index() function

print(my_num_tuple.index(650))
print(my_txt_tuple.index('drama'))

# .count() function

print(my_num_tuple.count(2))
print(my_txt_tuple.count('drama'))