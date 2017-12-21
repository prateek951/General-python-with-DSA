# Filters

grades = ['a','B','F','F','C']

def remove_fails(grade):
    return grade!='F'


print(list(filter(remove_fails,grades)))


# filter(testing_function,grades) 

# Here we have some kind of testing function on the basis of
# which we will filter the items
# Each of the items in the grades list will be passed to the testing function
# The testing function will return true or false for every grade that is passed to it
#  If grades passes the test then it will stay in the new filtered list otherwise will get rejected

# Exercises

# Filter out all the 1s in [1,2,33,2,11,1,1,1,3,4,2,1,1,2,2,1,3,2]

numbers = [1,2,33,2,11,1,1,1,3,4,2,1,1,2,2,1,3,2]

def filterOnes(number):
    return number != 1

print(list(filter(filterOnes,numbers)))
# Now 1s are filtered out of the array

# Filtering using for loop
# This is quite lengthy
filtered_grades = [];

for grade in grades:
        if grade!= 'F':
            filtered_grades.append(grade)

print(filtered_grades)

# Using the list comprehension methods

print([grade for grade in grades if grade!='F'])