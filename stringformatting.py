# STRING FORMATTING


num1 = 3.142	#Value of pie stored in num1

num2 = 10.2903948	

#PREVIOUS

print('Number 1 is',num1,'Number 2 is',num2)

# OUTPUT # Number 1 is 3.142 Number 2 is 10.2903948

#NEW WAY

print('Number 1 is {0} and Number 2 is {1}'.format(num1,num2))

# TO SET PRECISION WE CAN USE

#3 decimal places

print('Number 1 is {0:3} and Number 2 is {1}'.format(num1,num2))

# USING THE FORMAT-METHOD

print('Number 1 is {0:3f} and Number 2 is {1}'.format(num1,num2))

# USING THE F-STRINGS

# FOR GETTINGS 4 DECIMAL PLACES

print('Number 1 is {num1:4f} and Number 2 is {num2:4f}')














