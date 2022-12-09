# Lambda Functions (anonymous function)
# https://www.codecademy.com/courses/python-for-programmers/articles/lambda-functions-in-python

add_two = lambda x: x + 2

print(add_two(4))

# example 2:

import pandas as pd

df = pd.DataFrame({
    'name': ['Jackie', 'Luke', 'Mia'],
    'grades': [80, 72, 95]
})

# change data frame with a lambda function

df['grades'] = df['grades'].apply(lambda x: x * 1.2)

print(df)