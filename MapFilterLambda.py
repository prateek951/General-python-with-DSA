# Python code to test the working of map,filter and lambda

def cube(x):
    return x**2

print("MAP EXAMPLES")
cubes = map(cube,range(10))
# print(cubes) This is a map object
# Print it in the form of a list
print(list(cubes))


print("LAMBDA EXAMPLES")
print((lambda x: x**2)(5))
print((lambda x,y:x*y)(3,4))

print("Filter examples")
special_cubes = filter((lambda x:x>9 and x<60),cubes)
print(list(special_cubes))

# Find the number which is odd in the list
# and multiply them by 5 and create a new list

lister3 = [1,3,4,5,66]
lister4 = []

for item in lister3:
    if item %2 != 0:
        lister4 += [item*5]
print(lister4)
    