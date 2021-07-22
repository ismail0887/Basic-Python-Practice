#print line by line using read method

file1 = open('mytext.txt')

#line= file1.readline()

#while line!="":
   # print(line)
    #line= file1.readline()

for line in file1.readlines():
    print(line)

file1.close()