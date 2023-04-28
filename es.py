# Author : Evan Preston-Kelly
# Task 07 - takes in a filename (text file) from an agrument and outputs the number of e's in it
def read_file (textfile):
    file = open(textfile,"r")
    data = file.read()
    count = 0
    for i in data:
        if i =="e":
            count = count + 1
    return count

print(read_file('test.txt'))
