# Here use of module created before
import platform
import module
import math

print('User Defined Modules\n')

num1 = int(input('Please enter number1: '))
num2 = int(input('Please enter number2: '))
operator = input(f'type any operator from these {module.operators}: ')

module.calculate(num1, num2, operator)

checkOperator = "Yes" if module.operators.get(operator, "") else "No"
print(
    f'Lets check module has {operator} operator or not: {checkOperator}')


print('\n\nPre-Defined Modules\n')

op = platform.system()
print(
    f'The operating system installed in this machine: {op}. Using pre-defined module platform')

print(f'lets try to show pi value using math module: {math.pi}')

print(help('modules'))
