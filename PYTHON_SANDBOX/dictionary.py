# create dictionary and check duplicate item in it
person = {
    'name': 'madiha',
    'country': 'Pakistan',
    'passion': 'software engineer',
    'experience': 5,
    'country': 'Pakistan'
}

print(f' Dictionary created, no duplication in it: {person}')

# length fun in dictionary
print(
    f'the length of the this dictionary is {len(person)}, calculated using len()')

# print the value of a key in dictionary
print(f'the value of key "name" is {person["name"]}')

# get() values against keys
print(f'the value of key "name" is {person.get("name")}')

# get all the keys of the dictionary
print(f'Get all the keys of the dictionary are {person.keys()} using keys()')

# get all the values of the dictionary
print(
    f'Get all the values of the dictionary are {person.values()} using values()')

# items() return all the items (key with value) in the dictionary created in the dictionary
print(
    f'items() return all the items (key with value) in the dictionary created in the dictionary {person.items()}')

# check if key or value or item is in dictionary or not
if 'name' in person:
    print(f'key "{"name"}" is in dictionary "person"')

# update the value of a key in dictionary
person['experience'] = 5.5
print(
    f'update the value of a key "experience" in dictionary is {person['experience']}')

# using builtin update()
person.update({'experience': 5.5})
print(
    f'using update() to update the value {person["experience"]} against key "experience" in dictionary person')

#  add new item
person.update({'id': 10})
print(f'add new item in dictionary {person} using update()')

person['skills'] = 'Development'
print(f'add new item in dictionary {person} using [] method')

# Delete any item from dictionary
person.pop('skills')
print(f' delete "skills" from the {person} using pop()')

person.popitem()
print(f' delete by default last item from the {person} using popitem()')

del person['name']
print(
    f'delete name from dictionary using del check {person}. this also delete whole dic.')

person.clear()
print(f'make the whole data deleted from dic. check {person}')
