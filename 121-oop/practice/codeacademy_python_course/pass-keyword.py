# using the pass & break keywords

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']

# pass
print('\n :: pass example :: \n')

for name in names:
    if 'j' in name.lower():
        pass
    else:
        print(name)

# break
print('\n :: break example :: \n')

for name in names:
    if 'h' in name.lower():
        break
    else:
        print(name)

# continue
print('\n :: continue example :: \n')

for name in names:
    if 'h' in name.lower():
        continue
    else:
        print(name)