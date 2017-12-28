# Ternary operator in python
a,b = 10,20
min = a if a < b else b 
print(min)

# Direct method by using tuple dictionary and lambda

a,b = 10,20
#  Use tuple for selecting an item
print((b,a)[a<b])
# Use dictionary for selecting an item
print({True: a,False: b}[a<b])

# Lambda expression is more efficient than the above two
# reason is only one expression will be evaluated unlike the tuple and dictionary
print((lambda:b,lambda:a)[a<b]())

a,b = 10,20
print("Both a and b are equal" if a == b else "a is greater than b" if a>b else "b is greater than a")

a,b = 10,20

if a!= b:
    if a>b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")


# Operator functions in python
