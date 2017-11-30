ninjas = {}

while True:
	
	ninja_name = input('Enter the ninja name')

	ninja_belt = input('Enter the ninja belt')

	ninjas[ninja_name] = ninja_belt

	# Type y to stop entering ninjas

	choice = input('Want more ninjas')

	if choice == 'y':
	
		continue
	
	else:
		
		break

# NOW WE ARE HAVING A DICTIONARY OF NINJAS

def ninja_details(dictionary):
	
	# cycle through all the ninjas

	# Note a ninjas is a dictionary of key and values

	for key,val in dictionary.items():

		print(f'My name is {key} and I am a {val}-belter')


# INVOKE THE ninja_details function

ninja_details(ninjas)

