# Write a Python program to count the number of vowels in a string

def count_vowels(str):
    return sum(1 for char in str if char in 'aeiouAEIOU')


print(count_vowels('helloO'))
