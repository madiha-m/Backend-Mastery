long_str = '''use triple quote to format a long string, and this str is enclosed in it.'''
print(long_str)

print('Get 1st char from string, while we use 0 index, and consider string as array: ',
      long_str[0])
print('Get last char from string, while we use -1 index, and consider string as array: ',
      long_str[-1])

print('slice the string: ', long_str[0:5])

first_part = long_str[0:10]
last_part = long_str[-1:10]
full = f"First Part: {first_part}. Last Part: {last_part}"

print(full)

imp_points = '''
Falsy nMenues in Python 
1- \"\"  
2- 0 
3- None 
'''

print(imp_points)
