lorempointer = open('files/ipsum.txt')

# Point to the 50th position
# Set the file pointer at the 50th position
lorempointer.seek(50)

# From there onwards we want to read next 100 characters

# Here we have characters from the index 50 to 100(exclusive)
read_file = lorempointer.read(100)

print(read_file)


# Now we need to close the file otherwise we will suffer from performance hits if we do not close the file
# after we have read the file


# Remember to reposition the pointer at any arbitrary position after we have read the file completely
#  use seek(position) method here position is the index where we want to place our pointer again

lorempointer.close()

