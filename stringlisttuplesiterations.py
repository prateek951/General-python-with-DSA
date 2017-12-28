a = "This is a string"
print(a)

# In python we don't have arrays we make use of lists

# List need not be always homogeneous
# A single list can contain strings,integers as well as objects.
# Lists are mutable Strings are immutable
lister = [1,"a","string",1+2]
print(lister)


lister.append(6)
print(lister)
print(lister[1])    #prints the second element of the list
lister.pop()
print(lister)


# Tuples in python

# Sequence of immutable python objects
# Tuples are like lists
# Tuples once declared cannot be modified
# Faster than lists

tup = (1,"a","string",1+2)
print(tup)
print(tup[1])

# Iterations in python
# Using the for loops and the while loops
s = "Prateek"
for i in s:
    print(i)

# Iteration by a for loop on the list

lister2 = [1,"a",323+343,323.4,"string",True]

for item in lister2:
    print(item)

# Iteration by a for loop for the range
for item in range(0,10):
    print(item)

# Dictionaries in python

# Dictionary is similiar to hash maps in java
# The value can be accessed by a unique key in the dictionary

# Creating a new dictionary
d = dict()
# Add key value pairs to the dictionary
d['xyz'] = 2
d['abc'] = 5

# print the whole dictionary
print(d)

# print only the keys
print(d.keys())

# print only the values
print(d.values())

# iterate over the dictionary
for item in d:
    print("%s %d" %(item,d[item]))

# another method for iteration over a dictionary
for index,value in enumerate(d):
    print(index,value,d[value])

# Check if the key exists
print('xyz' in d) 

# delete the key value pair
del d['xyz']

print('xyz' in d)


