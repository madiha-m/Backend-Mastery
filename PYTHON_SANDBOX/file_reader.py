import os

# check if file exists
file = 'content.txt'
if os.path.exists(file):

    file_content = open(file, 'r')  # open file in read mode

    # read all content from the file
    print(f'\nRead whole content of the file: \n {file_content.read()}')

    # now cursor is at the end of file
    file_content.seek(0)  # Move cursor to the start

    # read 1st 5 characters of the file
    print(
        f'\nRead 1st 5 characters of content of the file: {file_content.read(5)}')

    # read file content line by line
    file_content.seek(0)  # Move cursor to the start

    # read single line from the file
    print(
        f'\nRead all lines from the file: \n {file_content.readlines()}')

    # read single line from the file
    file_content.seek(0)  # Move cursor to the start

    print(
        f'\nRead one line from the file: \n {file_content.readline()}')

    # read all lines from the file, iterate it
    file_content.seek(0)  # Move cursor to the start

    print('\nRead the content from the file line by line  using strip and for loop')

    for line in file_content:
        print(line.strip())

    # close the file
    file_content.close()

else:
    print(f'File {file} does not exist')
