# Dictionaries in Python
# https://www.codecademy.com/courses/python-for-programmers/articles/dictionaries-in-python

groceries = {
    'fruits': ['mangoes', 'bananas', 'kiwis'],
    'protein': ['quinoa', 'tofu', 'lentils'],
    'carbs': ['rice', 'pasta', 'bread'],
    'veggies': ['lettuce', 'cabbage', 'onions']
}

party_planning = {'Yes': 10,
                  'No': 15,
                  'Maybe': 30,
                  'Location': 'Our Backyard',
                  'Date': '2022/05/01'}
 
print(party_planning['Location']) # prints 'Our Backyard'

# update value

party_planning['Location'] = 'At the park'
print(party_planning['Location']) # now it is 'at the park'

# add new key-pair value
print(party_planning)
party_planning['Dress Code'] = 'Casual'
print(party_planning)

# len() works the same as other data collections

len(party_planning) # returns 6

# .update() method

shopping_list1 = {
    'jewelry': 'earrings',
    'clothes': 'jeans',
    'budget': 200
}

shopping_list2 = {
    'shoes': 'sandals',
    'budget': 350
}

shopping_list1.update(shopping_list2)

print(shopping_list1) 
# {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 350, 'shoes': 'sandals'}

# .keys() and .values() methods

keyShoppingList = shopping_list1.keys()
valShoppingList = shopping_list1.values()
print(keyShoppingList, valShoppingList)

# dict cheatsheet: 
# https://www.codecademy.com/learn/paths/learn-python-3/tracks/learn-python-3/modules/learn-python3-dictionaries/cheatsheet