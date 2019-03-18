from sys import argv
script,input_file=argv
out_file = open(input_file)

def print_all(file):
	print file.read()

def rewind(file):
	file.seek(0)

def print_line(line,file):
	print line,file.readline()




current_file = open(input_file,'w')

current_file.truncate()

line = "I once was a lonely litte boy as innocent as a rose petal then came the monsters to wreak my innocence They were successful upto some point"
current_file.write(line)

current_file = open(input_file)

print "first lets print whole file"

print_all(current_file)

print "let us rewind the file"

rewind(current_file)

print "lets print file one by one"

countline = 1

print_line(countline,current_file)

countline += 1

print_line(countline,current_file)

countline += 1

print_line(countline,current_file)

current_file.close()




def add(one,two):
    return one+two

def multiply(one,two):
    return one*two

def subtract(one,two):
    return one-two


total = add(5,multiply(5,subtract(5,5)))
 
print "total : %d"%(total) 














