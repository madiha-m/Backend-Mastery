file_name = 'content.txt'
# add more content in an existing file
file = open(file_name, 'a')
file.write(''' \n updated data
           Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
           Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
           It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
           It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
           ''')
file.close()

# update and replace the existing content in an existing file
file = open(file_name, 'w')
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
file.close()

# create new file
file = open('content_write.txt', 'x')
