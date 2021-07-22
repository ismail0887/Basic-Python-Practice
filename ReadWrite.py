file= open('mytext.txt')
#read all content of file
#print(file.read()) #it will read all content of file

#print(file.read(4)) # it will pick first 4 character of file

print(file.readline()) #it will print only first line

print(file.readline()) #it will print only second line

file.close()