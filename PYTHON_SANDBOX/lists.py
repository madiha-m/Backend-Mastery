# Define list
fruits = ['fig', 'banana', 'mango']

numbers = [1, 2, 3, 4]
print(fruits, numbers, fruits[2])

# update list item
numbers[3] = 'gg'
print('Updated single item: ', numbers)

numbers[1:3] = ['aa', 'bb', 'cc']
print('Updated multiple item [1:3]: ', numbers)

# add duplicate list item
numbers.insert(1, 'gg')
print(
    f'use insert() to add a duplicate item b/w 0 and 1 indexes :  {numbers}')
numbers.append('last item')
print(
    f'use append() and added new item added at end:  {numbers}')

# craete new list and extend the old list with new list
newFruitsList = ['cherry', 'apple']
fruits.extend(newFruitsList)
print(f'use extend() to add new list items at the end of old list: {fruits}')
newFruitsTuple = ('watermelon', 'grapes')
fruits.extend(newFruitsTuple)
print(f'use extend() to add new tuple items at the end of old list: {fruits}')
newFruitsDictionary = {'fruit': 'almonds'}
fruits.extend(newFruitsDictionary.values())
print(
    f'use extend() to add new Dictionary item at the end of old list: {fruits}')

# Delete / Remove list item from List
fruits.remove('banana')
print(f'remove specific item from list, apply remove(<item>): {fruits}')
fruits.pop()
print(f'remove last item from list, apply pop(): {fruits}')
fruits.pop(3)
print(f'remove specified index item from list, apply pop(<index>): {fruits}')
del fruits[2]
print(f'remove specified index item from list, apply del: {fruits}')
fruits.clear()
print(
    f'make the list empty, using remover(): {fruits}')
del fruits
print(
    f'remove entire list, apply del: {fruits}, and it gives error, as list deleted')
