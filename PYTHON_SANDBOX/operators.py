# Comparison operators
print('Comparison operators')
num1 = int(input('please enter 1st number:'))
num2 = int(input('please enter 2nd number:'))


# check equality
print(f'Check equality of 2 numbers: {num1 == num2}')

# check greater than other, greater than or equal to other
print(f'Check greater of 2 numbers: {num1 >= num2}')
print(f'Check greater than or equal to of 2 numbers: {num1 > num2}')

# check less than other, less than or equal to other
print(f'Check less than of 2 numbers: {num1 <= num2}')
print(f'Check less than or equal to of 2 numbers: {num1 < num2}')

# Logical operators
print('\nLogical operators')
print(f'check "and" operator: {num1 > 5 and num2 < 10}')
print(f'check "or" operator: {num1 > 5 or num2 < 7}')
print(f'check "not" operator: {not (num1 > 5 and num2 <= 9)}')

# additional operators
print('''additional operators ha 2 types\n
      - Identity Operators: Used to compare obj. It has 2 types \n
      -- is: compare 2 values, are those actually same value?\n
      -- is not: compare 2 values, are those not same value?\n
      - Membership Operators: Used to check sequence , if value is present in sequence or not. It has 2 types \n
      -- in: check value is present in sequence or not\n
      -- not in: check value is not present in sequence or not 
      ''')

list1 = ['fig', 'apple']
list2 = ['fig', 'apple']
list3 = list2

# Identity operator
print(
    f'test list1 and lis2 are equal: {list1 is list2}. Because both are different objects. Here use Identity operator')
print(
    f'test list1 and lis2 are not equal: {list1 is not list2}. Because both are different objects. Here use Identity operator')
print(
    f'is "Apple" not in the list {"apple" not in list1}. use identity operator')
# Membership operator
print(f'is "fig" in the list {"fig" in list1}. use membership operator')
print(
    f'is "fig" not in the list {"fig" not in list1}. use membership operator')
