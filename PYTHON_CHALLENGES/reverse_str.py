# Satement
print('Write a program that takes a string of lowercase characters as input and prints it in uppercase, reversed.\n')

# Solution
# take input in lowercase
user_data = input('Please enter the a string in lowercase.').lower()

# Make the lowercase data into upper case
uppercase_data = user_data.upper()

# Reverse the uppercase data
reversed_data = uppercase_data[::-1]

# Print the final output
print(reversed_data)
