# Statement
'''
    This function aims to create a new string by swapping the first and last characters of the given input_string.

    To achieve this, follow these steps:

    Check if the length of the input_string is less than 2. If so, return the input_string as is since swapping is not possible.
    Store the first character of the input_string in a variable.
    Replace the first character of the input_string with the last character.
    Replace the last character of the input_string with the stored first character.
    Return the modified input_string.
'''
print('Create a new string by swapping the first and last characters of the given input_string.')

# Solution
#  return input_string[-1] + input_string[1:-1] + input_string[0]


def swap_characters(input_string):
 # If the length of the input_string is less than 2, return as is
    if len(input_string) < 2:
        return input_string

    # Store the first character in a temp variable
    temp_char = input_string[0]

    # Convert string to list to modify characters
    str_list = list(input_string)  # Convert string to list
    str_list[0] = str_list[-1]     # Replace first character with last
    str_list[-1] = temp_char        # Replace last character with temp_char

    return "".join(str_list)


print(swap_characters('Hk kkkk jjj ouoi hkh p'))
