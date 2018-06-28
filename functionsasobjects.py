"""

The below behaviour is only shown in languages
like Python and Javascript and not in C and C++

Although they are created differently from normal variables, 
functions are just like any other kind of value. 
They can be assigned and reassigned to variables, and later
referenced by those names
"""

def multiply(a,b):
    return x*y

a = 4
b = 7
operation = multiply
print(operation(3,4))

# Functions can also be used as arguments of other functions

def add(x,y):
    return x+y

def do_twice(func,x,y):
    return func(func(x,y),func(x,y))

a = 5
b = 10
print(do_twice(add,a,b))

