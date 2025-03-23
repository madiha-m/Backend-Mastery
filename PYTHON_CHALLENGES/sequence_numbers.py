# Statement
print('Print the list of integers from  through  as a string, without spaces.\n')

if __name__ == "__main__":
    n = int(input('please enter a number: '))

    # 1st way
    print('\nusing for loop, use end="" to remove space')
    for i in range(1, n+1):
        print(i, end='')

    # 2nd way
    print(f'\n\nusing join() function: {"".join(map(str, range(1, n+1)))}')
