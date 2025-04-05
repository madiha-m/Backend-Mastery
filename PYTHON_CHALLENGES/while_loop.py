'''
    Write a program that gets one input, float number.
    Use a while loop to divide the input by 2 as long as the number is bigger or equal to 3.5.
    Print the first number that is smaller than 3.5.
'''

number = float(input())
while number >= 3.5:
    number /= 2
print(number)
