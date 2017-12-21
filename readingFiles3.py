# Another way of reading files but in this 
#  method we do not require to close the file

# Uptil now we have use the methods

# readlines for reading lines one by one using the lorempointer

# read with/without seek for reading upto particular number of bytes

# Now here we will use the with keyword 

# fp = open('files/sample.txt')

def sequenceFilter(line):
    return '>' not in line
    


with open('files/sample.txt') as fp:

    lines = fp.readlines()

    # Here we have read all the lines but we do not want that so we need to filter

    print(list(filter(sequenceFilter,lines)))

# carry on with our program down here

# Here in this approach there is no need for closing the files

