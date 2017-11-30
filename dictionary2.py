ninjas = {}
while True:
	
	ninja_name = input('Enter the ninja name')
	ninja_belt = input('Enter the ninja belt')
	ninjas[ninja_name] = ninja_belt
	choice = input('Want more ninjas')
	if choice == 'y':
	
		continue
	else:
		break

def ninja_details(dictionary):
	
	for key,val in dictionary.items():

		print(f'My name is {key} and I am a {val}-belter')

ninja_details(ninjas)

