# create a tuple
names = ('ali', 'asad', 'ahmed')
names = ('hhh')

print(
    f'created 2 tuples with same name, the 2nd tuple will be executed, as var name is just a reference to object {names}')

# difference b/w tuple and str
str = ('it is a string')
tuple = ('it is a tuple',)
print(
    f'ths is a string: {type(str)} and this is a tuple: {type(tuple)} we use , to make it tuple with single item')

# concatenate Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 7, 8)

allTuples = tuple1 + tuple2

# delete Tuple
del tuple1
print(f'After deletion Tuple {tuple1+tuple2}')
