# Write a Python program to find the maximum of three numbers
def max_number_with_condition(a1, a2, a3):
    if a1 > a2 and a1 > a3:
        return a1
    elif a2 > a1 and a2 > a3:
        return a2
    else:
        return a3


def max_number_with_fun(a1, a2, a3):
    return max(a1, a2, a3)


print(max_number_with_condition(1, 2, 3))
print(max_number_with_fun(1, 2, 3))
