# OPERATORS

# <,>,==,!=,=>,=<

age = int(input('Enter your age'))	#The user inputs the age but that age is of String type so using int() we can typecast it!
#CHECK FOR AGE
if age < 10:

	# If age is less than 10
	print('You are very young')

elif age < 40:
	# If age is greater or equal to 10 but less than 40
	print('You are somewhat mature')
else:
	# kind of catch all if above are false
	print('You are wise beyond dooubt!!')

meat = input('Do you eat fish?(y/n):')



if meat == 'y':

	print('You are a non-vegetarian')

else :

	print('You are a vegetarian')


		


