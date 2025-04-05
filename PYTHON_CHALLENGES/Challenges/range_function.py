'''
Create a range that starts at 0 and ends at 4
'''


def print_range(start, end, step):
    # Write your code here
    for i in range(start, end, step):
        print(i)


# Get input from user
start = int(input())
end = int(input())
step = int(input())

# Call the function
print(print_range(start, end, step))
