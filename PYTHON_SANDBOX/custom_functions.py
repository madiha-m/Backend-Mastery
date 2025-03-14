def greet():
    print("Hello, World!")
    print('hi girls why r u laughing')


greet()


# types of functions
print('''
      TYpes of Functions:
      1- Perform a task
      2- Return a value
      ''')


def get_greeting(name):
    return f'Hi {name}'


message = get_greeting('John')
file = open('content.txt', 'w')
file.write(message)


def chek_none():
    return '...'


print('this is none: ', chek_none())
