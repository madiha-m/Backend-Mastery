# Create function
def calculate(num1, num2, operator):
    operation = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed",
    }
    return print(operation.get(operator, "Invalid operator"))


# create dictionary here.
operators = {
    '+': '+',
    '-': '-',
    '*': '*',
    '/': '/',
    
}
