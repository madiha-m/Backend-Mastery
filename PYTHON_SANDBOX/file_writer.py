file_name = 'content.txt'
# add more content in an existing file
with open(file_name, 'a') as file:
    file.write(''' \n updated data
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
            ''')

print('content append successfully')

# Replace all content in an existing file
with open(file_name, 'w') as file:
    file.write(''' This is new content , it is replacing old content.
            thi is 2nd line.
            ""
            ""
            "check"
            1
            2
            3
            ghj nnnn
            ''')

print('Existing content replaced successfully')

# Overwi=rite existing file completely
with open('content_write.txt', 'x') as file:
    file.write('Another content in the file')

print('File successfully overwritten')
