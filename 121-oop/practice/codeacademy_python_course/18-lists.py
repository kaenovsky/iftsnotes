# Lists in Python
# https://www.codecademy.com/courses/python-for-programmers/articles/lists-in-python

lst1 = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst2 = [0, 1, 2, 3, 4]
lst3 = ['I love tofu', 'I also love curry']

print(lst1[0])

# slicing
print(lst1[4:6])

# len
print(len(lst1))
print(len(lst2))
print(len(lst3))

# append
lst1.append(99)
print(lst1)

# remove
lst1.remove(62)
print(lst1)

# pop
lst1.pop()
print(lst1)
lst1.pop(0)
print(lst1)