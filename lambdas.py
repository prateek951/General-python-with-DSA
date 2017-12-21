
# Lambdas are just like anonymous functions
# Use lambdas for those functions which will be called only once
# and will not be used again.

numbers = [1,2,3,4,5,6]

def square(number):
    return number**2

# lambda n:n**2   it is just like an inline anonymous function
    
print(list(map(square,numbers)))

print(list(map(lambda n:n**2,numbers)))


