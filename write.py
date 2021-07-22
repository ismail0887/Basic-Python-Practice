# Read the file and store all data into list
# reverse the list
# Write the List back to the file
with open('mytext.txt', 'r') as reader: # r is used to read
    content= reader.readlines() # it will read the file
    reversed(content) # it will reverse the conent
    with open('mytext.txt', 'w') as writter: # w will write
        for line in reversed(content):
            writter.write(line) # it will reversed conents present in file

