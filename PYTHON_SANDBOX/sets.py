# create sets
fruits = {'orange', 'banana', 'apple', 'banana'}
print(
    f' sets remove the duplicates, only show elements uniquely from its collection: {fruits}')
print(f'Length of fruits sets : {len(fruits)}. Duplicates not included.')

# create set using tuple
names = set(('ali', 'ana', 'ans', 'ali'))
print(f' set created from tuple: {names}')

# Items unable to access in sets
fruits = {'orange', 'apple', 'mango'}
for i in fruits:
    print(i)  # prints each item in the set

# Add item in sets
fruits.add('lemon')
print(f'Add an item in sets, using add() method: {fruits}')

newFruits = {'fig', 'almond'}
fruits.update(newFruits)
print(
    f'Add multiple items in sets, using update() method: {fruits}')

# Remove item from sets
fruits.remove('fig')
print(f'Remove an item from sets, using remove() method: {fruits}')

# fruits.remove('Item not part of set, while using remove()')
# print(f'Item not part of set so cannot delete it. gives KeyError for {fruits}')

fruits.discard('Item not part of set, while using discard()')
print(
    f'Item not part of set so cannot delete it. not show any error for {fruits}')

# Pop() applied
fruits.pop()
print(f'Pop() method removes an item from sets, {fruits}')

# clear()
fruits.clear()
print(f'clear() method removes all items from sets, {fruits}')

# del method
del fruits
print(f'del method removes all items from sets, {fruits}')
