
# Setting up the reference to the file

lorempointer = open('files/ipsum.txt')

# for line in lorempointer:
#     print(line)

for line in lorempointer:
    print(line.rstrip())

# Setting the pointer to the initial position at the index 0
lorempointer.seek(0)
# Setting up the lines as a reference to the lorempointer

# This reads one line at a time.
lines = lorempointer.readlines()

print(lines)
print(list(line for line in lines))