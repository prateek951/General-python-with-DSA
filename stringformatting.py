# STRING FORMATTING

num1 = 3.142	#Value of pie is stored in num1
num2 = 10.2903948	

#Normal way of printing out to console

print('Number 1 is',num1,'Number 2 is',num2)

# OUTPUT # Number 1 is 3.142 Number 2 is 10.2903948

#New way using the format method

print('Number 1 is {0} and Number 2 is {1}'.format(num1,num2))

# To set precision we can use : after the index and specifying the number of decimal places!!
#3 decimal places

print('Number 1 is {0:3} and Number 2 is {1}'.format(num1,num2))

# Using the format method

print('Number 1 is {0:3f} and Number 2 is {1}'.format(num1,num2))

# Using the f-strings for getting the numbers upto 4 decimal places
print('Number 1 is {num1:4f} and Number 2 is {num2:4f}')














