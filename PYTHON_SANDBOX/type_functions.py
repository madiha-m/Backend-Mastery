# Build in type function
print(type(4))
print(type(range(4)))

# Iterable
print('''
      \'Iterable things in python\'
      1-  range ()
      2-  list
      3-  tuple
      4-  string
      ''')
for x in range(4):
    print(x)

# While loop
command = ""
while command.lower() != "quit":
    command = input(">>>")
    print("ECHO", command)

# show even numbers from 1-10
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f'The total umber of Even Numbers are: {count}')
