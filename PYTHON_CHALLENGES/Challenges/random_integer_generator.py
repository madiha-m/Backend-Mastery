'''
    Write a function named random_int that takes two integers, a and b, 
    and returns a random integer within the range of a and b (inclusive).

    Example: random_int(5, 9) could return 5, 6, 7, 8, or 9.
'''
import random


def random_int(a, b):
    return random.randint(a, b)


print(random_int(2, 3))
